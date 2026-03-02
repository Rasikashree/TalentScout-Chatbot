#!/bin/bash
# TalentScout Run Script for macOS/Linux

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[ERROR] Virtual environment not found!"
    echo "Please run ./setup.sh first"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "[ERROR] .env file not found!"
    echo "Please create .env file and add OPENAI_API_KEY"
    exit 1
fi

# Check if OPENAI_API_KEY is set
if grep -q "your_openai_api_key_here" .env; then
    echo "[ERROR] OPENAI_API_KEY not configured in .env"
    echo "Please edit .env and add your actual API key"
    exit 1
fi

# Run Streamlit app
echo ""
echo "Starting TalentScout Hiring Assistant..."
echo "Opening: http://localhost:8501"
echo ""
streamlit run app.py
