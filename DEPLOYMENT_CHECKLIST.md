# 📋 Streamlit Cloud Deployment Checklist

## Pre-Deployment Setup

### ✅ Repository Setup
- [x] `.env` file is in `.gitignore` (NOT committed)
- [x] `requirements.txt` has all dependencies
- [x] `app.py` exists in root directory
- [x] `src/` folder with chatbot code exists
- [x] No secrets/API keys in committed files

### ✅ Git Repository
- [ ] GitHub account created (https://github.com)
- [ ] New repository created: `TalentScout-Chatbot`
- [ ] Repository is PUBLIC (required for free tier)
- [ ] Code committed locally: `git add -A && git commit -m "Initial commit"`

### ✅ Streamlit Cloud
- [ ] Streamlit Cloud account created (https://share.streamlit.io)
- [ ] GitHub authorized with Streamlit Cloud
- [ ] Repository pushed to GitHub

---

## Exact Steps to Deploy

### Step 1: Verify Local Setup ✓
```bash
# Check git status
git status

# Should show: "On branch main" and "nothing to commit"
```

### Step 2: Push to GitHub
```bash
# Add GitHub remote (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/TalentScout-Chatbot.git

# Set main branch
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 3: Deploy on Streamlit Cloud
1. Visit: https://share.streamlit.io
2. Click "New app"
3. Select:
   - Repository: `YOUR_USERNAME/TalentScout-Chatbot`
   - Branch: `main`
   - Main file path: `app.py`
4. Click "Deploy"

### Step 4: Add Secrets
1. Click profile icon (top right)
2. Click "Settings"
3. Click "Secrets"
4. Paste this:
```
OPENAI_API_KEY=sk-proj-your_actual_api_key_here
LLM_MODEL=gpt-3.5-turbo
```
5. Click "Save"
6. Wait 2 minutes

### Step 5: Access Your App
```
https://YOUR_USERNAME-talentscout-chatbot.streamlit.app
```

---

## 🚀 Quick Command Reference

```bash
# Check git status
git status

# Add all files
git add -A

# Commit
git commit -m "Ready for Streamlit Cloud deployment"

# Add GitHub remote (do this once)
git remote add origin https://github.com/YOUR_USERNAME/TalentScout-Chatbot.git

# Set branch to main (do this once)
git branch -M main

# Push to GitHub
git push -u origin main

# After first push, just use:
git push
```

---

## 📝 Files Ready for Deployment

✅ `app.py` - Main Streamlit app
✅ `config.py` - Configuration
✅ `requirements.txt` - Dependencies
✅ `src/chatbot.py` - Chatbot logic
✅ `src/prompts.py` - Prompt templates
✅ `src/utils.py` - Utility functions
✅ `.env` - **IN .gitignore** (secrets)
✅ `.streamlit/config.toml` - Streamlit config

---

## ⚠️ Important Security Notes

🔒 **NEVER commit:**
- `.env` file (has your API key!)
- API keys or tokens
- Passwords or credentials

✅ **DO commit:**
- `requirements.txt` (dependencies)
- `app.py` and source files
- Configuration (without secrets)

✅ **ADD in Streamlit Cloud:**
- Environment variables/secrets
- API keys
- Credentials

---

## 🆘 Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| "Repository not found" | Check GitHub repo is public and URL is correct |
| "API key not working" | Wait 2 min after adding secret, then refresh app |
| "ModuleNotFoundError" | Add missing package to `requirements.txt` and push |
| "App won't load" | Check logs in Streamlit Cloud dashboard |
| "Connection refused" | Verify OPENAI_API_KEY is set in Streamlit secrets |

---

## ✅ Final Verification Checklist

Before visiting your deployed app:
- [ ] GitHub repo created and public
- [ ] Code pushed to `main` branch
- [ ] Streamlit Cloud app deployed (check logs)
- [ ] Secrets added: `OPENAI_API_KEY` and `LLM_MODEL`
- [ ] Waited 2 minutes after adding secrets
- [ ] App URL is accessible

---

## 🎉 After Deployment

### Workflow for Updates
```bash
# Make changes locally
# Test with: streamlit run app.py

# Commit and push
git add -A
git commit -m "Describe your changes"
git push

# Your app auto-updates in 2-5 minutes!
```

### Monitor Your App
- Streamlit Cloud dashboard shows deployment status
- Logs available for debugging
- Real-time error messages

---

## 📞 Need Help?

- **Streamlit Docs:** https://docs.streamlit.io/deploy/streamlit-cloud
- **GitHub Docs:** https://docs.github.com
- **Streamlit Community:** https://discuss.streamlit.io

---

**You're ready to deploy! Follow the exact steps above. Good luck! 🚀**
