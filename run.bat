@echo off
REM TalentScout Run Script for Windows

echo Checking prerequisites...

REM Check if virtual environment exists
if not exist "venv\" (
    echo [ERROR] Virtual environment not found!
    echo Please run setup.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if .env exists
if not exist ".env" (
    echo [ERROR] .env file not found!
    echo Please create .env file and add OPENAIN_API_KEY
    pause
    exit /b 1
)

REM Check if OPENAI_API_KEY is configured
findstr "your_openai_api_key_here" .env >nul
if not errorlevel 1 (
    echo [ERROR] OPENAI_API_KEY not configured in .env
    echo Please edit .env and add your actual API key
    pause
    exit /b 1
)

echo.
echo Starting TalentScout Hiring Assistant...
echo Opening: http://localhost:8501
echo.

streamlit run app.py
