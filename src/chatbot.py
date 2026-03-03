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
    from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
except ImportError:
    try:
        from langchain.chat_models import ChatOpenAI
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
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
        self.llm_available = True
        self.last_llm_error: Optional[str] = None

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

    def _safe_invoke(self, messages: List[Any]) -> Optional[str]:
        """Invoke LLM safely and return None if the provider is unavailable."""
        try:
            response = self.llm.invoke(messages)
            self.llm_available = True
            self.last_llm_error = None
            return response.content
        except Exception as exc:
            self.llm_available = False
            self.last_llm_error = str(exc)
            return None

    def _fallback_greeting(self) -> str:
        """Deterministic greeting when LLM is unavailable."""
        return (
            "Hello! Welcome to TalentScout 👋\n\n"
            "I’ll guide you through a short screening process. "
            "First, please share your **full name** (first and last name)."
        )

    def _fallback_clarification(self, field: str) -> str:
        """Fallback clarification prompts by field."""
        prompts = {
            "full_name": "Please provide your full name (first and last name).",
            "email": "Please provide a valid email address (example: name@example.com).",
            "phone": "Please provide a valid phone number with country code if possible.",
            "experience_years": "Please enter your years of experience as a number (for example: 3 or 5.5).",
            "desired_position": "Please share the role you are applying for (at least 3 characters).",
            "location": "Please share your current city and country.",
            "tech_stack": "Please list your core technologies (for example: Python, Django, PostgreSQL).",
        }
        return prompts.get(field, f"Please provide your {field.replace('_', ' ')}.")

    def _fallback_technical_questions(self) -> List[str]:
        """Generate deterministic technical questions when LLM is unavailable."""
        tech_stack = self.candidate_info.get("tech_stack", [])
        experience = self.candidate_info.get("experience_years", 0)

        base_questions = [
            "Describe a recent technical project you worked on and your specific contributions.",
            "How do you approach debugging when a production issue is reported?",
            "What practices do you use to write maintainable and testable code?",
        ]

        stack_questions = []
        for tech in tech_stack[:3]:
            stack_questions.append(
                f"In {tech}, what are the most important best practices you follow in real projects?"
            )

        if experience >= 5:
            base_questions.append(
                "How do you design scalable systems and mentor junior engineers in your team?"
            )
        elif experience <= 1:
            base_questions.append(
                "How do you learn a new technology quickly when assigned an unfamiliar task?"
            )

        questions = stack_questions + base_questions
        return questions[:5]

    def _fallback_ending(self) -> str:
        """Deterministic ending when LLM is unavailable."""
        name = self.candidate_info.get("full_name", "Candidate")
        return (
            f"Thank you, {name}! Your interview responses have been recorded. ✅\n\n"
            "We’ve captured your profile details and technical answers. "
            "Our recruitment team will review your application and reach out within **5-7 business days** with next steps."
        )

    def _fallback_redirect(self) -> str:
        """Fallback redirect when input is unclear."""
        if self.conversation_stage == "information" and self.current_field_index < len(self.required_fields):
            field = self.required_fields[self.current_field_index]
            return self._get_next_information_request(field)
        if self.conversation_stage == "questions":
            return self._get_next_technical_question()
        return "Could you please share a bit more detail so I can help you better?"

    def start_conversation(self) -> str:
        """Start the chatbot conversation with a greeting."""
        greeting_message = GREETING_PROMPT.format(company_name="TalentScout")

        # Create system and greeting messages
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=greeting_message),
        ]

        greeting_response = self._safe_invoke(messages) or self._fallback_greeting()

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

        response = self._safe_invoke(messages)
        return response or self._fallback_clarification(field)

    def _generate_technical_questions(self) -> List[str]:
        """Generate technical questions based on candidate's tech stack."""
        tech_stack = self.candidate_info.get("tech_stack", [])
        experience = self.candidate_info.get("experience_years", 0)
        position = self.candidate_info.get("desired_position", "")
        name = self.candidate_info.get("full_name", "")

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

        response_text = self._safe_invoke(messages)
        if not response_text:
            return self._fallback_technical_questions()

        # Extract questions from the response
        questions = self._extract_questions(response_text)
        return questions or self._fallback_technical_questions()

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

        ending_message = self._safe_invoke(messages) or self._fallback_ending()

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

        response = self._safe_invoke(messages)
        return response or self._fallback_redirect()

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
