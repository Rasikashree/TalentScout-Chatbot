# 🚀 Quick Start Guide - TalentScout

Get TalentScout Hiring Assistant running in 5 minutes!

## **Windows Users**

### 1. Download or Clone the Project
```bash
git clone <repository-url>
cd talentscout_chatbot
```

### 2. Run Setup Script
Double-click `setup.bat` or open terminal and run:
```bash
setup.bat
```

### 3. Configure API Key
- Open `.env` file with any text editor
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=sk-your-actual-key-here
  ```
- Get a key from [OpenAI Platform](https://platform.openai.com/api-keys)

### 4. Start the App
Double-click `run.bat` or run:
```bash
run.bat
```

✅ App opens at `http://localhost:8501`

---

## **macOS / Linux Users**

### 1. Download or Clone the Project
```bash
git clone <repository-url>
cd talentscout_chatbot
```

### 2. Run Setup Script
```bash
chmod +x setup.sh run.sh
./setup.sh
```

### 3. Configure API Key
```bash
nano .env
# or
vi .env
```

Add your OpenAI API key:
```
OPENAI_API_KEY=sk-your-actual-key-here
```

### 4. Start the App
```bash
./run.sh
```

✅ App opens at `http://localhost:8501`

---

## **Manual Setup (All Platforms)**

If scripts don't work, follow these steps:

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate (Windows)
venv\Scripts\activate
# OR activate (macOS/Linux)
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env and add your API key

# 5. Run the app
streamlit run app.py
```

---

## **Get OpenAI API Key (2 minutes)**

1. Go to https://platform.openai.com/api-keys
2. Click "Create new secret key"
3. Copy the key (you won't see it again!)
4. Paste in `.env` file: `OPENAI_API_KEY=sk-...`

**Free Credits:** New accounts get $5 in free credits (expires in 3 months)

---

## **Use the Chatbot**

1. Click **"Start Conversation"** button
2. Answer the bot's questions about:
   - Your name
   - Email and phone
   - Years of experience
   - Desired position
   - Current location
   - Tech stack (programming languages, frameworks, etc.)

3. Bot generates 3-5 **custom technical questions** based on your tech stack

4. Answer the questions and complete the interview!

5. Type **"goodbye"** or **"exit"** to end anytime

---

## **Common Issues**

### "OpenAI API key not found"
**Solution:** Make sure `.env` has `OPENAI_API_KEY=sk-...` and it's OUTSIDE quotes

### "ModuleNotFoundError"
**Solution:** Run `pip install -r requirements.txt` again

### "Port 8501 already in use"
**Solution:** 
- Windows: `streamlit run app.py --server.port 8502`
- macOS/Linux: Edit to different port

### "Slow responses"
**Check:**
- API key is valid
- You have internet connection
- OpenAI service is working (check status.openai.com)

---

## **Troubleshooting Checklist**

- [ ] Python 3.8+ installed? (`python --version`)
- [ ] Virtual environment created? (`venv` folder exists)
- [ ] Virtual environment activated? (terminal shows `(venv)`)
- [ ] Dependencies installed? (no errors with `pip install`)
- [ ] `.env` file created? (in project root)
- [ ] API key added to `.env`? (correctly formatted)
- [ ] Internet connection working?

---

## **What Happens to My Data?**

✅ **Privacy-First Approach:**
- Your personal data is **anonymized** when saved
- Names stored as first initial only (e.g., "J***")
- No email/phone/address stored in logs
- All data saved locally in `data/` folder
- You can delete anytime

---

## **Next Steps**

### 📖 Want to Learn More?
- Read [README.md](README.md) - Complete documentation
- Check [PROMPT_ENGINEERING.md](PROMPT_ENGINEERING.md) - How AI works
- Review [CHALLENGES_SOLUTIONS.md](CHALLENGES_SOLUTIONS.md) - Development details

### 🚀 Ready to Deploy?
- See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for cloud deployment options

### 🤝 Want to Contribute?
- Read [CONTRIBUTING.md](CONTRIBUTING.md)
- Check issues for improvements

### 🐛 Found a Bug?
- Open an issue on GitHub
- Include error message and steps to reproduce

---

## **System Requirements**

| Requirement | Minimum | Recommended |
|------------|---------|-------------|
| Python | 3.8 | 3.10+ |
| RAM | 2GB | 4GB+ |
| Storage | 500MB | 1GB |
| Internet | Broadband | High-speed |
| OS | Windows/Mac/Linux | Windows 10+ / macOS 10.14+ / Ubuntu 20.04+ |

---

## **Architecture Overview**

```
┌─────────────────┐
│  Your Browser   │  (http://localhost:8501)
└────────┬────────┘
         │
┌────────▼────────┐
│ Streamlit UI    │
│   (app.py)      │
└────────┬────────┘
         │
┌────────▼────────────────┐
│   TalentScout Chatbot   │
│   (src/chatbot.py)      │
└────────┬────────────────┘
         │
    ┌────▼─────┐
    │  OpenAI  │  (GPT-3.5 Turbo)
    │   API    │
    └──────────┘
```

---

## **Key Features Checklist**

✅ Smart greeting and conversation flow  
✅ Validates email, phone, experience  
✅ Parses tech stack automatically  
✅ Generates intelligent technical questions  
✅ Difficulty adjusted to experience level  
✅ Saves anonymized candidate data  
✅ Professional, friendly tone  
✅ Graceful conversation ending  
✅ Progress tracking  
✅ Mobile-responsive UI  

---

## **Quick Commands Reference**

```bash
# Setup
python -m venv venv
source venv/bin/activate  # macOS/Linux or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Run
streamlit run app.py

# Test
python test_chatbot.py

# Debug
streamlit run app.py --logger.level=debug

# Format code
black src/ app.py

# Check style
flake8 src/ app.py
```

---

## **Version Info**

- **TalentScout Version:** 1.0.0
- **Python:** 3.8+
- **Streamlit:** Latest
- **Last Updated:** March 2, 2026

---

## **Questions?**

📧 Email: support@talentscout.example.com  
📚 Docs: Check [README.md](README.md)  
💬 Issues: GitHub Issues tracker  

---

**Ready to go?** 🎯

👉 **Run setup now:** 
- Windows: Double-click `setup.bat`
- Mac/Linux: Run `./setup.sh`

Happy hiring! 🚀
