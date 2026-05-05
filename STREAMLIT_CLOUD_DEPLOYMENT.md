# 🚀 Streamlit Cloud Deployment - Step-by-Step Guide

## Prerequisites
- ✅ GitHub account (free)
- ✅ Streamlit Cloud account (free)
- ✅ Your project pushed to GitHub

---

## Step 1: Prepare Your GitHub Repository

### 1.1 Initialize Git (if not already done)
```bash
git init
git add -A
git commit -m "Initial commit - TalentScout Chatbot"
```

### 1.2 Create GitHub Repository
1. Go to [github.com/new](https://github.com/new)
2. Repository name: `TalentScout-Chatbot`
3. Description: "AI Hiring Assistant Chatbot"
4. Make it **Public** (required for free Streamlit Cloud)
5. Click "Create repository"

### 1.3 Push Your Code to GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/TalentScout-Chatbot.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

---

## Step 2: Create Streamlit Cloud Account

1. Visit [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in with GitHub"**
3. Authorize Streamlit to access your GitHub
4. Accept the terms and create account

---

## Step 3: Deploy Your App

### 3.1 Start Deployment
1. On Streamlit Cloud dashboard, click **"New app"**
2. Select:
   - **Repository:** `YOUR_USERNAME/TalentScout-Chatbot`
   - **Branch:** `main`
   - **Main file path:** `app.py`

3. Click **"Deploy"**

*Deployment takes 2-5 minutes. You'll see logs in real-time.*

---

## Step 4: Add Environment Secrets

### ⚠️ IMPORTANT: Do NOT commit `.env`!

Your `.env` is already in `.gitignore`, so secrets are NOT in GitHub. You need to add them in Streamlit Cloud:

1. Click your **profile icon** (top right)
2. Select **"Settings"**
3. Go to **"Secrets"** section
4. Paste this exactly:

```
OPENAI_API_KEY=sk-proj-your_actual_api_key_here
LLM_MODEL=gpt-3.5-turbo
```

5. Click **"Save"**
6. **Wait 1-2 minutes** for changes to propagate

---

## Step 5: Access Your Deployed App

Your app is now live at:
```
https://YOUR_USERNAME-talentscout-chatbot.streamlit.app
```

**Example:** `https://rasikashree-talentscout-chatbot.streamlit.app`

---

## 🎯 What Happens Next

### Auto-Redeployment
- Every time you `git push` to `main` branch
- Streamlit Cloud automatically redeploys your app
- Takes 2-5 minutes

### Example Workflow:
```bash
# Make changes locally
git add .
git commit -m "Update chatbot features"
git push origin main

# Your app auto-deploys in 2-5 minutes!
```

---

## ✅ Verify Deployment Works

1. Open your app URL
2. Test the chatbot:
   - Enter candidate information
   - Start a conversation
   - Verify responses are working

---

## 🆘 Troubleshooting

### ❌ "App not loading"
**Solution:**
1. Check deployment logs (app settings → logs)
2. Verify `app.py` exists in repository root
3. Ensure all files are committed: `git status`
4. Push any missing files: `git push`

### ❌ "API key not working"
**Solution:**
1. Go to Settings → Secrets
2. Verify secret name is exactly: `OPENAI_API_KEY`
3. Wait 2 minutes for changes to take effect
4. Refresh your app: `Ctrl+R`

### ❌ "ModuleNotFoundError"
**Solution:**
1. Check `requirements.txt` has all dependencies
2. Verify it includes:
   - streamlit
   - langchain
   - langchain-openai
   - openai
   - python-dotenv
3. Push changes to GitHub

### ❌ "500 Internal Server Error"
**Solution:**
1. Check logs in Streamlit Cloud dashboard
2. Common causes:
   - Missing environment variables
   - Wrong API key
   - Missing dependencies
3. Commit fixes and push: `git push`

---

## 📊 Monitoring Your App

### View Real-time Logs
1. Streamlit Cloud dashboard
2. Click your app
3. Click **"Settings"** → **"Logs"**

### View App Status
- **Green indicator** = Running
- **Red indicator** = Error (check logs)
- **Yellow indicator** = Deploying

---

## 💾 Backing Up Your Code

Your code is automatically backed up on GitHub! No action needed.

---

## 🔐 Security Checklist

- ✅ `.env` file in `.gitignore` (not in GitHub)
- ✅ Secrets added to Streamlit Cloud (not in code)
- ✅ API key never committed to repository
- ✅ Public repository (required for free tier)

---

## 💡 Pro Tips

### 1. Custom Domain (Paid Plans)
- Upgrade to Pro/Business
- Add custom domain like `talentscout.yourdomain.com`

### 2. Increase Resource Limits (Paid Plans)
- Free tier: 1 GB RAM
- Pro tier: 3 GB RAM
- Business: Unlimited

### 3. Private Apps (Paid Plans)
- Make repository private
- Control who can access your app

### 4. Scheduled Runs
- Run specific functions on schedule
- Useful for data updates

---

## 📞 Support Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Streamlit Community:** https://discuss.streamlit.io
- **GitHub Issues:** Your repo's Issues tab
- **Status Page:** https://status.streamlit.io

---

## 🎉 You're All Set!

Once deployed, your app will be:
- ✅ Live on the internet
- ✅ Auto-updating with each GitHub push
- ✅ Running 24/7
- ✅ Completely free!

**Enjoy your deployed TalentScout Chatbot!** 🚀
