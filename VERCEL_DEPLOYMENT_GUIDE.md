# 🚀 Vercel Deployment Guide for TalentScout Chatbot

## ⚠️ Important: Vercel Limitations with Streamlit

Vercel is optimized for **serverless functions**, not **long-running Streamlit apps**. However, Vercel does support Docker deployments which work better for Streamlit.

---

## 🎯 Two Deployment Methods for Vercel

### Method 1: Docker Deployment (RECOMMENDED ✅)
**Pros:**
- Best performance for Streamlit on Vercel
- Supports long-running sessions
- Full WebSocket support
- Better state management

**Cons:**
- Requires Docker setup
- Slightly longer build time

### Method 2: Serverless Function Wrapper (Alternative)
**Pros:**
- Faster deployment
- Simpler configuration

**Cons:**
- May have timeout issues
- Limited session persistence
- WebSocket issues possible

---

## 🐳 Method 1: Docker Deployment (Recommended)

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Update vercel.json
File already updated with correct configuration.

### Step 4: Update Dockerfile
Your Dockerfile is already configured correctly.

### Step 5: Deploy to Vercel
```bash
vercel --prod
```

### Step 6: Set Environment Variables in Vercel
1. Go to: https://vercel.com/dashboard
2. Select your project: `talentscout-chatbot`
3. Go to "Settings" → "Environment Variables"
4. Add:
   ```
   OPENAI_API_KEY=sk-proj-your_actual_api_key_here
   LLM_MODEL=gpt-3.5-turbo
   ```
5. Save and redeploy

### Step 7: Your App is Live!
```
https://talentscout-chatbot.vercel.app
```

---

## 🔗 Method 2: GitHub Integration (Auto-Deploy)

### Step 1: Create Vercel Account
1. Visit: https://vercel.com/signup
2. Sign up with GitHub

### Step 2: Import Your Repository
1. Go to: https://vercel.com/new
2. Click "Import Git Repository"
3. Select: `Rasikashree/TalentScout-Chatbot`
4. Click "Import"

### Step 3: Configure Project
- **Project Name:** `talentscout-chatbot`
- **Framework Preset:** `Other`
- **Root Directory:** `./` (leave as default)

### Step 4: Set Environment Variables
Before deploying:
1. Click "Environment Variables"
2. Add:
   ```
   OPENAI_API_KEY=sk-proj-your_actual_api_key_here
   LLM_MODEL=gpt-3.5-turbo
   ```
3. Click "Deploy"

### Step 5: Access Your App
Your app will be available at:
```
https://talentscout-chatbot.vercel.app
```

---

## 📋 Recommended: Step-by-Step (GitHub Auto-Deploy)

### Step 1: Ensure All Files Are Committed
```bash
git status
# Should show "nothing to commit"
```

### Step 2: Make Sure GitHub Repo is Up-to-Date
```bash
git push origin main
# Verify all files are on GitHub
```

### Step 3: Go to Vercel
1. Visit: https://vercel.com/new
2. Click "Continue with GitHub"
3. Authorize Vercel to access your GitHub

### Step 4: Select Your Repository
1. Search for: `TalentScout-Chatbot`
2. Click to select it

### Step 5: Configure Deployment
- **Framework Preset:** Leave as "Other"
- **Build Command:** `pip install -r requirements.txt`
- **Output Directory:** Leave empty
- **Install Command:** Leave empty

### Step 6: Add Secrets
Before clicking "Deploy":

1. Click "Environment Variables"
2. Add the following:
   ```
   Key: OPENAI_API_KEY
   Value: sk-proj-your_actual_api_key_here
   ```
   
   ```
   Key: LLM_MODEL
   Value: gpt-3.5-turbo
   ```

3. Click "Deploy"

### Step 7: Wait for Deployment
⏳ Vercel will build and deploy your app (takes 3-5 minutes)

### Step 8: Access Your Live App
Once deployment completes, visit:
```
https://talentscout-chatbot.vercel.app
```

---

## ✅ After Deployment

### Auto-Redeploy on GitHub Push
Every time you push to GitHub:
```bash
git push origin main
```

Vercel automatically redeploys your app! ✨

### Monitor Deployment
1. Go to: https://vercel.com/dashboard
2. Click your project
3. View deployments and logs

---

## 🆘 Troubleshooting

### ❌ "Deployment failed"
**Solution:**
1. Check Vercel build logs
2. Verify `requirements.txt` has all dependencies
3. Ensure `.env` is in `.gitignore` (secrets not in GitHub)
4. Try redeploying

### ❌ "503 Service Unavailable"
**Solution:**
1. Check environment variables are set correctly
2. Verify `OPENAI_API_KEY` is valid
3. Wait 2-3 minutes for app to fully start
4. Refresh browser

### ❌ "App won't load"
**Solution:**
1. Check deployment logs in Vercel dashboard
2. Verify all files were pushed to GitHub
3. Check if API key is expiring

### ❌ "Module not found"
**Solution:**
1. Add missing package to `requirements.txt`
2. Push to GitHub: `git push`
3. Vercel auto-redeploys

---

## 📝 Vercel-Specific Configuration Files

### `.vercelignore` (Optional)
```
# Optional: Specify files to ignore
.git
node_modules
venv/
__pycache__/
*.pyc
.streamlit/
data/
```

### `vercel.json` (Already Updated)
Configured to handle Streamlit deployment

---

## 🔒 Security Checklist

- ✅ `.env` file in `.gitignore` (not committed)
- ✅ Secrets added in Vercel dashboard (not in code)
- ✅ API key never in GitHub
- ✅ Repository is public (required)
- ✅ `OPENAI_API_KEY` set in Vercel environment

---

## 📊 Vercel Account Considerations

### Free Plan
- ✅ $0/month
- ✅ Up to 100 deployments/day
- ✅ 1 concurrent build
- ✅ 50GB bandwidth/month
- ✅ Perfect for testing/development

### Pro Plan ($20/month)
- ✅ Unlimited deployments
- ✅ 4 concurrent builds
- ✅ 1TB bandwidth/month
- ✅ Priority support
- ✅ Custom domains

---

## 💡 Pro Tips

1. **Check Deployment Status:**
   - Real-time logs in Vercel dashboard
   - Status indicator: Green = Live, Red = Error

2. **View App Logs:**
   - Dashboard → Project → Deployments → Logs

3. **Rollback If Issues:**
   - Dashboard → Deployments → Right-click deployment → Promote

4. **Custom Domain:**
   - Settings → Domains → Add custom domain

---

## 📞 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Vercel Support:** https://vercel.com/support
- **Python on Vercel:** https://vercel.com/docs/platforms/python
- **Streamlit Docs:** https://docs.streamlit.io

---

## 🎉 You're Ready!

Your TalentScout Chatbot is ready to deploy on Vercel! Choose either:
- **Docker Method** (better performance)
- **GitHub Auto-Deploy** (easier setup)

Both will get your app live in minutes! 🚀

---

**Follow the "GitHub Auto-Deploy" method for the fastest, easiest setup!**
