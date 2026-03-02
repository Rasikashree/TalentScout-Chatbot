"""
Utility functions for TalentScout Hiring Assistant chatbot
Includes data validation, storage, and helper functions
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, Any, List, Optional
import validators
from config import CANDIDATES_DIR, RESPONSES_DIR, CONVERSATION_ENDING_KEYWORDS


def validate_email(email: str) -> bool:
    """Validate email format."""
    return validators.email(email) is True


def validate_phone(phone: str) -> bool:
    """Validate phone number format (basic validation)."""
    # Remove common separators
    cleaned = re.sub(r"[\s\-\+\(\).]", "", phone)
    # Check if it contains at least 7 digits
    return len(re.findall(r"\d", cleaned)) >= 7


def validate_years_of_experience(years_str: str) -> tuple[bool, Optional[int]]:
    """Validate and extract years of experience."""
    try:
        years = int(years_str.split()[0])
        return 0 <= years <= 70, years if 0 <= years <= 70 else None
    except (ValueError, IndexError):
        return False, None


def is_conversation_ending(user_input: str) -> bool:
    """Check if user input contains conversation-ending keywords."""
    user_lower = user_input.lower().strip()
    return any(keyword in user_lower for keyword in CONVERSATION_ENDING_KEYWORDS)


def extract_tech_stack(tech_input: str) -> List[str]:
    """Extract and parse tech stack from user input."""
    # Split by comma and clean up
    technologies = [item.strip() for item in tech_input.split(",")]
    # Remove empty strings
    return [tech for tech in technologies if tech]


def save_candidate_info(candidate_info: Dict[str, Any]) -> str:
    """Save candidate information to JSON file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"candidate_{timestamp}.json"
    filepath = os.path.join(CANDIDATES_DIR, filename)

    # Anonymize sensitive data (keep only partial info)
    safe_info = {
        "timestamp": timestamp,
        "name_initial": candidate_info.get("full_name", "Unknown")[0] + "***",
        "experience_years": candidate_info.get("experience_years"),
        "desired_position": candidate_info.get("desired_position"),
        "location": candidate_info.get("location"),
        "tech_stack": candidate_info.get("tech_stack", []),
    }

    with open(filepath, "w") as f:
        json.dump(safe_info, f, indent=2)

    return filename


def save_conversation_response(
    candidate_name: str, questions: List[str], responses: Dict[str, str]
) -> str:
    """Save candidate's responses to technical questions."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"responses_{timestamp}.json"
    filepath = os.path.join(RESPONSES_DIR, filename)

    response_data = {
        "timestamp": timestamp,
        "candidate_name_initial": candidate_name[0] + "***" if candidate_name else "Unknown",
        "questions": questions,
        "responses": responses,
    }

    with open(filepath, "w") as f:
        json.dump(response_data, f, indent=2)

    return filename


def format_conversation_history(messages: List[Dict]) -> str:
    """Format conversation history for context management."""
    formatted = ""
    for msg in messages:
        role = msg.get("role", "unknown").upper()
        content = msg.get("content", "")
        formatted += f"{role}: {content}\n"
    return formatted


def sanitize_user_input(user_input: str) -> str:
    """Clean and sanitize user input."""
    # Remove leading/trailing whitespace
    sanitized = user_input.strip()
    # Remove multiple spaces
    sanitized = " ".join(sanitized.split())
    # Remove special characters that might cause issues
    sanitized = re.sub(r"[<>\'\"\\]", "", sanitized)
    return sanitized


def parse_json_response(response_text: str) -> Optional[Dict]:
    """Safely parse JSON from LLM response."""
    try:
        # Try to find JSON in the response
        json_match = re.search(r"\{[^{}]*\}", response_text, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
    except json.JSONDecodeError:
        pass
    return None


def get_candidate_info_progress(candidate_info: Dict[str, Any]) -> tuple[int, int]:
    """Calculate progress of information gathering."""
    required_fields = [
        "full_name",
        "email",
        "phone",
        "experience_years",
        "desired_position",
        "location",
        "tech_stack",
    ]
    completed = sum(1 for field in required_fields if candidate_info.get(field))
    return completed, len(required_fields)


def create_context_message(candidate_info: Dict[str, Any], messages: List[Dict]) -> str:
    """Create a context message for the LLM based on current state."""
    context = "Current Candidate Information:\n"
    context += f"- Name: {candidate_info.get('full_name', 'Not provided')}\n"
    context += f"- Email: {candidate_info.get('email', 'Not provided')}\n"
    context += f"- Experience: {candidate_info.get('experience_years', 'Not provided')} years\n"
    context += f"- Desired Position: {candidate_info.get('desired_position', 'Not provided')}\n"
    context += f"- Tech Stack: {', '.join(candidate_info.get('tech_stack', ['Not provided']))}\n"

    return context


def calculate_experience_level(years: int) -> str:
    """Calculate experience level based on years of experience."""
    if years < 1:
        return "Entry-level"
    elif 1 <= years < 3:
        return "Junior"
    elif 3 <= years < 7:
        return "Mid-level"
    elif 7 <= years < 12:
        return "Senior"
    else:
        return "Principal/Lead"


def get_difficulty_level_for_questions(experience_years: int) -> str:
    """Get appropriate difficulty level for technical questions."""
    level = calculate_experience_level(experience_years)
    if level == "Entry-level":
        return "Basic (fundamentals and common concepts)"
    elif level == "Junior":
        return "Intermediate (practical application and some advanced concepts)"
    elif level == "Mid-level":
        return "Advanced (deep understanding and best practices)"
    elif level == "Senior":
        return "Expert (architecture, optimization, and complex problem-solving)"
    else:
        return "Principal-level (system design, technology decisions, mentoring)"
