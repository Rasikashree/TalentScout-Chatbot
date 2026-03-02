#!/bin/bash
# TalentScout Setup Script for macOS/Linux

echo ""
echo "========================================"
echo "TalentScout - Hiring Assistant Chatbot"
echo "Setup & Installation Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

echo "[✓] Python found"
python3 --version

# Create virtual environment
echo ""
echo "[*] Creating Python virtual environment..."
python3 -m venv venv

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to create virtual environment"
    exit 1
fi

echo "[✓] Virtual environment created"

# Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[*] Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo "[*] Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi

# Setup .env file
if [ ! -f .env ]; then
    echo "[*] Creating .env file from template..."
    cp .env.example .env
    echo "[!] Please edit .env and add your OPENAI_API_KEY"
    echo "[!] You can get an API key from https://platform.openai.com/api-keys"
else
    echo "[✓] .env file already exists"
fi

echo ""
echo "========================================"
echo "[✓] Setup Complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "1. Edit .env file and add your OPENAI_API_KEY"
echo "2. Run: streamlit run app.py"
echo "3. Open browser to http://localhost:8501"
echo ""
