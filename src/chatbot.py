"""
Main Chatbot Logic for TalentScout Hiring Assistant
Handles conversation flow, LLM integration, and information gathering
"""

import os
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
import json

# LLM Integration - Use LangChain for flexibility
try:
    from langchain_openai import ChatOpenAI
    from langchain.schema import HumanMessage, SystemMessage, AIMessage
except ImportError:
    from langchain.chat_models import ChatOpenAI
    from langchain.schema import HumanMessage, SystemMessage, AIMessage

from config import (
    LLM_API_KEY,
    LLM_MODEL,
    REQUIRED_CANDIDATE_INFO,
    CONVERSATION_ENDING_KEYWORDS,
)
from src.prompts import (
    SYSTEM_PROMPT,
    GREETING_PROMPT,
    INFORMATION_GATHERING_PROMPTS,
    TECH_QUESTION_GENERATION_PROMPT,
    ENDING_PROMPT,
    FALLBACK_PROMPT,
)
from src.utils import (
    validate_email,
    validate_phone,
    validate_years_of_experience,
    is_conversation_ending,
    extract_tech_stack,
    save_candidate_info,
    save_conversation_response,
    sanitize_user_input,
    get_difficulty_level_for_questions,
    get_candidate_info_progress,
)


class TalentScoutChatbot:
    """
    Main chatbot class for TalentScout Hiring Assistant.
    Manages conversation flow, information gathering, and technical question generation.
    """

    def __init__(self, api_key: Optional[str] = None, model: str = LLM_MODEL):
        """
        Initialize the chatbot with LLM configuration.

        Args:
            api_key: OpenAI API key (uses env variable if not provided)
            model: LLM model to use (default: gpt-3.5-turbo)
        """
        self.api_key = api_key or LLM_API_KEY
        self.model = model

        # Initialize LLM
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. Set OPENAI_API_KEY environment variable."
            )

        self.llm = ChatOpenAI(
            api_key=self.api_key,
            model_name=model,
            temperature=0.7,
            max_tokens=1024,
        )

        # Conversation state
        self.conversation_history: List[Dict[str, str]] = []
        self.candidate_info: Dict[str, Any] = {}
        self.current_field_index = 0
        self.required_fields = [
            "full_name",
            "email",
            "phone",
            "experience_years",
            "desired_position",
            "location",
            "tech_stack",
        ]
        self.is_completed = False
        self.technical_questions: List[str] = []
        self.question_responses: Dict[str, str] = {}
        self.current_question_index = 0
        self.conversation_stage = "greeting"  # greeting, information, questions, completed

    def start_conversation(self) -> str:
        """Start the chatbot conversation with a greeting."""
        greeting_message = GREETING_PROMPT.format(company_name="TalentScout")

        # Create system and greeting messages
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=greeting_message),
        ]

        response = self.llm.invoke(messages)
        greeting_response = response.content

        # Add to conversation history
        self.conversation_history.append({"role": "assistant", "content": greeting_response})
        self.conversation_stage = "information"

        return greeting_response

    def process_user_input(self, user_input: str) -> Tuple[str, bool]:
        """
        Process user input and generate appropriate response.

        Args:
            user_input: The user's input message

        Returns:
            Tuple of (response, should_end_conversation)
        """
        # Sanitize input
        user_input = sanitize_user_input(user_input)

        # Check for conversation ending keywords
        if is_conversation_ending(user_input):
            return self._end_conversation(), True

        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_input})

        # Process based on current stage
        if self.conversation_stage == "information":
            response = self._gather_information(user_input)
        elif self.conversation_stage == "questions":
            response = self._process_question_response(user_input)
        else:
            response = self._get_fallback_response(user_input)

        # Add assistant response to history
        self.conversation_history.append({"role": "assistant", "content": response})

        return response, False

    def _gather_information(self, user_input: str) -> str:
        """Gather candidate information through conversation."""
        # Get current field
        if self.current_field_index < len(self.required_fields):
            current_field = self.required_fields[self.current_field_index]

            # Validate and store the input
            is_valid, processed_value = self._validate_field(current_field, user_input)

            if is_valid:
                self.candidate_info[current_field] = processed_value
                self.current_field_index += 1

                # Check if we gathered all information
                if self.current_field_index >= len(self.required_fields):
                    # Generate technical questions
                    self.technical_questions = self._generate_technical_questions()
                    self.conversation_stage = "questions"
                    self.current_question_index = 0

                    return self._get_next_technical_question()

                # Get next question
                next_field = self.required_fields[self.current_field_index]
                return self._get_next_information_request(next_field)
            else:
                # Ask for clarification
                return self._get_clarification_request(current_field, user_input)

        return "All information has been gathered. Ready for technical questions."

    def _validate_field(
        self, field: str, user_input: str
    ) -> Tuple[bool, Optional[Any]]:
        """Validate a specific field."""
        if field == "full_name":
            # Validate name (at least 2 characters)
            if len(user_input) >= 2 and len(user_input.split()) >= 2:
                return True, user_input
            return False, None

        elif field == "email":
            if validate_email(user_input):
                return True, user_input
            return False, None

        elif field == "phone":
            if validate_phone(user_input):
                return True, user_input
            return False, None

        elif field == "experience_years":
            is_valid, years = validate_years_of_experience(user_input)
            return is_valid, years

        elif field == "desired_position":
            # Accept any non-empty input
            if len(user_input.strip()) >= 3:
                return True, user_input
            return False, None

        elif field == "location":
            # Accept any non-empty input
            if len(user_input.strip()) >= 2:
                return True, user_input
            return False, None

        elif field == "tech_stack":
            tech_stack = extract_tech_stack(user_input)
            if len(tech_stack) >= 1:
                return True, tech_stack
            return False, None

        return False, None

    def _get_next_information_request(self, field: str) -> str:
        """Get the next information request message."""
        previous_name = self.candidate_info.get("full_name", "there")

        prompts = INFORMATION_GATHERING_PROMPTS.copy()
        if field == "email":
            message = prompts[field].format(name=previous_name)
        else:
            message = INFORMATION_GATHERING_PROMPTS.get(
                field, f"Could you please provide your {field.replace('_', ' ')}?"
            )

        return message

    def _get_clarification_request(self, field: str, user_input: str) -> str:
        """Get a clarification request for invalid input."""
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"The user provided '{user_input}' for the field '{field.replace('_', ' ')}'. "
                f"This doesn't seem valid. Ask them politely to provide valid information for this field."
            ),
        ]

        response = self.llm.invoke(messages)
        return response.content

    def _generate_technical_questions(self) -> List[str]:
        """Generate technical questions based on candidate's tech stack."""
        tech_stack = self.candidate_info.get("tech_stack", [])
        experience = self.candidate_info.get("experience_years", 0)
        position = self.candidate_info.get("desired_position", "")
        name = self.candidate_info.get("full_name", "")

        difficulty = get_difficulty_level_for_questions(experience)

        prompt = TECH_QUESTION_GENERATION_PROMPT.format(
            name=name,
            experience_years=experience,
            desired_position=position,
            tech_stack=", ".join(tech_stack),
        )

        messages = [
            SystemMessage(
                content="You are an expert technical interviewer. Generate focused, relevant technical questions."
            ),
            HumanMessage(content=prompt),
        ]

        response = self.llm.invoke(messages)
        response_text = response.content

        # Extract questions from the response
        questions = self._extract_questions(response_text)
        return questions

    def _extract_questions(self, response_text: str) -> List[str]:
        """Extract questions from LLM response."""
        lines = response_text.split("\n")
        questions = []

        for line in lines:
            # Look for numbered or bulleted questions
            line = line.strip()
            if line and (line[0].isdigit() or line.startswith("-") or line.startswith("•")):
                # Remove numbering/bullets
                question = (
                    line.lstrip("0123456789.-•) ")
                    .strip()
                    .replace("**", "")
                    .replace("*", "")
                )
                if len(question) > 10:
                    questions.append(question)

        return questions[:5]  # Return max 5 questions

    def _get_next_technical_question(self) -> str:
        """Get the next technical question."""
        if self.current_question_index < len(self.technical_questions):
            question = self.technical_questions[self.current_question_index]
            question_number = self.current_question_index + 1
            total_questions = len(self.technical_questions)

            return f"**Question {question_number}/{total_questions}:** {question}"
        else:
            return self._end_conversation()

    def _process_question_response(self, user_input: str) -> str:
        """Process response to a technical question."""
        if self.current_question_index < len(self.technical_questions):
            current_question = self.technical_questions[self.current_question_index]
            self.question_responses[str(self.current_question_index)] = user_input

            self.current_question_index += 1

            if self.current_question_index < len(self.technical_questions):
                return self._get_next_technical_question()
            else:
                # All questions answered
                self.conversation_stage = "completed"
                return self._end_conversation()

        return "Thank you for your responses!"

    def _end_conversation(self) -> str:
        """End the conversation gracefully."""
        name = self.candidate_info.get("full_name", "Candidate")
        position = self.candidate_info.get("desired_position", "technology")

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"End the conversation with {name} who applied for {position}. "
                f"Thank them, summarize what we discussed (information gathering and {self.current_question_index} technical questions), "
                f"and explain next steps: their profile will be reviewed and they'll hear back within 5-7 business days. "
                f"Be warm and encouraging."
            ),
        ]

        response = self.llm.invoke(messages)
        ending_message = response.content

        # Save candidate information
        if self.candidate_info:
            save_candidate_info(self.candidate_info)

        # Save responses
        if self.question_responses:
            save_conversation_response(
                self.candidate_info.get("full_name", "Unknown"),
                self.technical_questions,
                self.question_responses,
            )

        self.is_completed = True
        return ending_message

    def _get_fallback_response(self, user_input: str) -> str:
        """Get a fallback response for unclear input."""
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=f"The user input was: '{user_input}'. "
                f"This seems unclear or off-topic. "
                f"Respond helpfully to redirect the conversation while staying professional."
            ),
        ]

        response = self.llm.invoke(messages)
        return response.content

    def get_progress(self) -> Dict[str, Any]:
        """Get current conversation progress."""
        info_completed, info_total = get_candidate_info_progress(self.candidate_info)

        return {
            "stage": self.conversation_stage,
            "information_gathered": info_completed,
            "information_total": info_total,
            "questions_answered": self.current_question_index,
            "questions_total": len(self.technical_questions),
            "is_completed": self.is_completed,
        }

    def get_candidate_info(self) -> Dict[str, Any]:
        """Get gathered candidate information."""
        return self.candidate_info.copy()

    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get conversation history."""
        return self.conversation_history.copy()
