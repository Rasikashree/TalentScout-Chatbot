# TalentScout - Intelligent Hiring Assistant Chatbot

![TalentScout](https://img.shields.io/badge/TalentScout-v1.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Project Overview

**TalentScout** is an intelligent hiring assistant chatbot designed for recruitment agencies specializing in technology placements. The chatbot automates the initial screening process by gathering candidate information and generating tailored technical questions based on each candidate's specific tech stack.

### Key Features

✅ **Intelligent Conversation Flow** - Natural, context-aware interactions  
✅ **Information Gathering** - Collects essential candidate details  
✅ **Dynamic Question Generation** - Creates tailored technical questions  
✅ **Tech Stack Analysis** - Recognizes and evaluates diverse technologies  
✅ **Data Privacy** - Anonymized data storage and GDPR-compliant practices  
✅ **Professional UI** - Clean, intuitive Streamlit interface  
✅ **Fallback Mechanisms** - Handles unexpected inputs gracefully  

## 🏗️ Architecture

```
talentscout_chatbot/
├── app.py                 # Main Streamlit application
├── config.py              # Configuration and constants
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── src/
│   ├── chatbot.py         # Core chatbot logic with LLM integration
│   ├── prompts.py         # LLM prompt templates
│   └── utils.py           # Utility functions
├── data/
│   ├── candidates/        # Anonymized candidate information
│   └── responses/         # Candidate responses to questions
├── prompts/               # Prompt engineering documentation
└── README.md              # This file
```

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (or compatible LLM)
- pip (Python package manager)

### Step 1: Clone/Download the Repository

```bash
git clone <repository-url>
cd talentscout_chatbot
```

### Step 2: Create Python Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example
cp .env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
LLM_MODEL=gpt-3.5-turbo
```

**Getting an OpenAI API Key:**
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API keys section
4. Create a new API key
5. Copy it to your `.env` file

### Step 5: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## 💬 Usage Guide

### Starting a Conversation

1. **Launch the UI** - Run `streamlit run app.py`
2. **Click "Start Conversation"** - The assistant will greet you
3. **Follow the prompts** - Answer questions about your background

### Conversation Stages

**Stage 1: Information Gathering**
- Full Name
- Email Address
- Phone Number
- Years of Experience
- Desired Position(s)
- Current Location
- Tech Stack (programming languages, frameworks, databases, tools)

**Stage 2: Technical Questions**
- Based on your tech stack, you'll receive 3-5 tailored questions
- Answer each question to the best of your ability
- Questions get progressively detailed

**Stage 3: Completion**
- Thank you message with next steps
- Information is securely stored (anonymized)
- You'll hear back within 5-7 business days

### Exiting the Conversation

To gracefully end the conversation, type any of these:
- "goodbye"
- "bye"
- "exit"
- "quit"
- "thank you"

## 🔧 Technical Specifications

### Technologies Used

| Technology | Version | Purpose |
|-----------|---------|---------|
| Python | 3.8+ | Core language |
| Streamlit | Latest | Web UI framework |
| LangChain | 0.1.1 | LLM orchestration |
| OpenAI | 1.3.5 | Language model API |
| python-dotenv | 1.0.0 | Environment management |

### LLM Configuration

- **Model**: GPT-3.5 Turbo (configurable)
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Max Tokens**: 1024 (per response)
- **Context Window**: Maintained throughout conversation

## 📊 Data Handling & Privacy

### Data Collection

The chatbot collects:
- Basic information (name, contact details)
- Professional background (experience, skills)
- Technical assessment responses

### Data Storage

- **Location**: `data/candidates/` and `data/responses/`
- **Format**: JSON files with anonymized data
- **Anonymization**: 
  - Names stored as first letter + asterisks (e.g., "J***")
  - No sensitive financial information collected
  - No password or credentials stored

### GDPR Compliance

✅ Explicit consent gathering  
✅ Data minimization principles  
✅ Secure storage with anonymization  
✅ Easy data deletion options  
✅ Privacy policy compliance  

### Security Best Practices

1. **API Key Management**
   - Never commit `.env` files to version control
   - Use environment variables for sensitive data
   - Rotate keys regularly

2. **Data Protection**
   - Personal data is anonymized
   - No sensitive information is logged
   - Regular security audits

3. **User Privacy**
   - Transparent data usage
   - Opt-out mechanisms for data storage
   - Compliance with local regulations

## 📝 Prompt Engineering

### Design Philosophy

The prompts are crafted to:
1. **Guide the LLM** - Clear instructions for desired behavior
2. **Maintain Context** - Information carried throughout conversation
3. **Adapt to User Input** - Flexible handling of variations
4. **Ensure Coherence** - Consistent tone and professionalism

### Key Prompts

#### System Prompt
Sets the overall tone and role of the assistant. Defines conversation boundaries and ensures the AI stays focused on hiring assistance.

#### Information Gathering Prompts
Tailored requests for each type of information. Example:
```
"Could you please list the technologies you are proficient in? 
Please mention programming languages, frameworks, databases, 
and tools you work with."
```

#### Technical Question Generation
Dynamically creates questions based on:
- Candidate's tech stack
- Years of experience (determines difficulty)
- Target position
- Industry best practices

#### Context Management
Maintains conversation state and provides relevant history to the LLM for coherent follow-ups.

### Prompt Optimization Techniques

1. **Few-shot Examples** - Providing examples of desired outputs
2. **Role Definition** - Clear persona for the assistant
3. **Instruction Clarity** - Specific, unambiguous directions
4. **Token Efficiency** - Concise yet complete prompts

## 🔄 Conversation Flow Diagram

```
START
  ↓
GREETING → Introduce self and purpose
  ↓
INFORMATION GATHERING
  ├→ Full Name
  ├→ Email
  ├→ Phone
  ├→ Experience
  ├→ Desired Position
  ├→ Location
  └→ Tech Stack
  ↓
TECHNICAL QUESTION GENERATION
  ├→ Analyze tech stack
  ├→ Determine difficulty level
  └→ Generate 3-5 questions
  ↓
QUESTION ANSWERING
  ├→ Q1 → Response
  ├→ Q2 → Response
  ├→ Q3 → Response
  ├→ Q4 → Response
  └→ Q5 → Response
  ↓
COMPLETION
  ├→ Thank candidate
  ├→ Save anonymized data
  ├→ Explain next steps
  └→ END
```

## 🛠️ Configuration

Edit `config.py` to customize:

```python
# LLM Settings
LLM_MODEL = "gpt-3.5-turbo"  # Change to gpt-4, llama, etc.

# Conversation Settings
MAX_CONVERSATION_LENGTH = 50
CONVERSATION_ENDING_KEYWORDS = [...]

# Information Requirements
REQUIRED_CANDIDATE_INFO = [...]

# Tech Stack Categories
TECH_STACK_CATEGORIES = {
    "programming_languages": [...],
    "frameworks": [...],
    # ... more
}
```

## 📈 Advanced Features

### 1. Sentiment Analysis (Bonus)

The chatbot includes built-in sentiment analysis:
```python
# In prompts.py
SENTIMENT_ANALYSIS_PROMPT = """..."""
```

Monitor candidate sentiment during assessment for hiring insights.

### 2. Context Management

Advanced context tracking maintains conversation coherence:
- Conversation history preservation
- Information progress tracking
- Fallback mechanisms for confusion

### 3. Tech Stack Recognition

Intelligent parsing of diverse tech stacks:
- Programming languages
- Frameworks and libraries
- Databases and data tools
- Cloud platforms and DevOps tools

## 🐛 Troubleshooting

### Common Issues

**Issue: "OpenAI API key not found"**
```
Solution: Create .env file and add OPENAI_API_KEY=your_key
```

**Issue: "Module not found" errors**
```
Solution: Ensure virtual environment is activated and all dependencies installed
pip install -r requirements.txt
```

**Issue: Streamlit not starting**
```
Solution: 
streamlit run app.py --logger.level=debug
Check for port conflicts (default: 8501)
```

**Issue: Poor question quality**
```
Solution: 
- Ensure clear tech stack input
- Check API model selection
- Review LLM_MODEL in config.py
```

## 📚 Project Structure Details

### `src/chatbot.py`
**Main chatbot logic**
- `TalentScoutChatbot` class - Core conversational AI
- Information validation and gathering
- Technical question generation
- Conversation state management

### `src/prompts.py`
**LLM prompt templates**
- System prompt defining assistant behavior
- Information gathering prompts
- Question generation templates
- Context and clarification prompts

### `src/utils.py`
**Utility functions**
- Data validation (email, phone, experience)
- Data storage and retrieval
- Conversation history formatting
- Information anonymization

### `config.py`
**Configuration management**
- API settings
- Conversation parameters
- Tech stack categories
- Data storage paths

### `app.py`
**Streamlit UI**
- User interface components
- Session state management
- Message rendering
- Progress tracking and display

## 🚀 Deployment Options

### Local Deployment (Current)
- Fast setup and testing
- Perfect for development
- Limited concurrent users

### Cloud Deployment Options

**Option 1: Heroku (Free tier deprecated, use alternatives)**

**Option 2: AWS**
```bash
# Deploy on AWS EC2 or Lambda
# Use AWS Elastic Beanstalk for easy deployment
# Requirements: AWS account and CLI configured
```

**Option 3: Google Cloud Run**
```bash
# Deploy containerized app on Google Cloud
# Create Dockerfile (included in bonus)
gcloud run deploy talentscout --source .
```

**Option 4: Streamlit Cloud (Recommended)**
```
1. Push code to GitHub
2. Visit streamlit.io/cloud
3. Connect your GitHub repository
4. Deploy with one click!
```

**Option 5: Azure**
```bash
# Use Azure App Service for straightforward deployment
# Benefits: App Service plans, auto-scaling, monitoring
```

## 📊 Monitoring & Analytics

### Metrics to Track
- Number of candidates interacted with
- Average conversation duration
- Questions answered per session
- Tech stack distribution
- Conversation completion rate

### Logs Location
- Candidate data: `data/candidates/`
- Responses: `data/responses/`
- Application logs: `.streamlit/logs/`

## 🔐 Security Checklist

- [ ] API key stored in `.env`, not in code
- [ ] `.env` file in `.gitignore`
- [ ] Data anonymization implemented
- [ ] No sensitive data in logs
- [ ] HTTPS enabled for deployment
- [ ] Rate limiting configured
- [ ] Input validation on all fields

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:

1. **Multilingual Support** - Add language detection and translation
2. **Advanced UI** - Custom CSS themes and responsive design
3. **Sentiment Analysis** - Emotional tone assessment
4. **Analytics Dashboard** - Recruitment metrics visualization
5. **Interview Recording** - Audio/video capture capabilities
6. **Resume Integration** - Auto-fill from uploaded resumes

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👥 Support & Contact

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: support@talentscout.example.com
- Documentation: Check the `docs/` folder

## 🎯 Future Roadmap

**v1.1 (Next Release)**
- [ ] Multilingual support (Spanish, French, Mandarin)
- [ ] Video interview capability
- [ ] Resume parsing integration
- [ ] Scheduling for follow-up interviews

**v1.2**
- [ ] Machine learning-based candidate ranking
- [ ] Integration with ATS systems
- [ ] Advanced sentiment analysis dashboard
- [ ] Customizable company branding

**v2.0**
- [ ] Multi-turn interviews with different assessors
- [ ] Real-time collaboration features
- [ ] Advanced analytics and reporting
- [ ] Mobile app

## ✨ Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI](https://openai.com/)
- Prompt engineering inspired by best practices in LLM applications
- Community feedback and contributions

---

**Made with ❤️ for the recruitment industry**

*Last Updated: March 2, 2026*
*Version: 1.0.0*
