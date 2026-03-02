@echo off
REM TalentScout Setup Script for Windows
echo.
echo ========================================
echo TalentScout - Hiring Assistant Chatbot
echo Setup & Installation Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [✓] Python found
python --version

REM Create virtual environment
echo.
echo [*] Creating Python virtual environment...
python -m venv venv

if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo [✓] Virtual environment created
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo [*] Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

REM Setup .env file
if not exist .env (
    echo [*] Creating .env file from template...
    copy .env.example .env
    echo [!] Please edit .env and add your OPENAI_API_KEY
    echo [!] You can get an API key from https://platform.openai.com/api-keys
) else (
    echo [✓] .env file already exists
)

echo.
echo ========================================
echo [✓] Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Edit .env file and add your OPENAI_API_KEY
echo 2. Run: streamlit run app.py
echo 3. Open browser to http://localhost:8501
echo.
pause
