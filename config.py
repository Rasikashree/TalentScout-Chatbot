"""
Configuration settings for TalentScout Hiring Assistant Chatbot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# LLM Configuration
LLM_API_KEY = os.getenv("OPENAI_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-3.5-turbo")

# Conversation Settings
MAX_CONVERSATION_LENGTH = 50  # Maximum number of exchanges
CONVERSATION_ENDING_KEYWORDS = [
    "goodbye",
    "bye",
    "exit",
    "quit",
    "thank you",
    "thanks for your time",
    "that's all",
    "no more questions",
]

# Candidate Information Requirements
REQUIRED_CANDIDATE_INFO = [
    "full_name",
    "email",
    "phone",
    "experience_years",
    "desired_position",
    "location",
    "tech_stack",
]

# Technical Stack Categories
TECH_STACK_CATEGORIES = {
    "programming_languages": [
        "Python",
        "Java",
        "JavaScript",
        "TypeScript",
        "C++",
        "C#",
        "Go",
        "Rust",
        "PHP",
        "Ruby",
    ],
    "frameworks": [
        "Django",
        "Flask",
        "FastAPI",
        "React",
        "Vue.js",
        "Angular",
        "Spring Boot",
        "Express.js",
        "NextJs",
    ],
    "databases": [
        "PostgreSQL",
        "MySQL",
        "MongoDB",
        "Redis",
        "Elasticsearch",
        "DynamoDB",
    ],
    "tools": [
        "Docker",
        "Kubernetes",
        "Git",
        "AWS",
        "GCP",
        "Azure",
        "Jenkins",
        "GitHub Actions",
    ],
}

# Application Settings
APP_TITLE = "TalentScout Hiring Assistant"
APP_DESCRIPTION = "Intelligent Hiring Assistant for Technology Placements"
COMPANY_NAME = "TalentScout Recruitment Agency"

# Data Storage
DATA_DIR = "data"
CANDIDATES_DIR = os.path.join(DATA_DIR, "candidates")
RESPONSES_DIR = os.path.join(DATA_DIR, "responses")

# Create directories if they don't exist
os.makedirs(CANDIDATES_DIR, exist_ok=True)
os.makedirs(RESPONSES_DIR, exist_ok=True)
