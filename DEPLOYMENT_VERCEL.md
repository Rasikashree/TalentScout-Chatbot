# TalentScout Chatbot - Vercel Deployment Guide

## ⚠️ Important: Streamlit on Vercel Limitations

**Streamlit apps have limited compatibility with Vercel** because:
- Vercel is designed for **serverless functions** (max 60-300s execution)
- Streamlit requires **persistent server connections**
- Streamlit uses **WebSockets** for real-time updates
- Session state management is problematic on serverless platforms

## 🎯 Recommended Deployment Options (Ranked)

### ✅ Option 1: Streamlit Cloud (BEST - Free & Native)
**Pros:**
- Native Streamlit support
- Free tier available
- Automatic deployments from GitHub
- Zero configuration needed
- Perfect for your use case

**Steps:**
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "Deploy an app" → Select your repository
4. Add `OPENAI_API_KEY` in deployment secrets
5. Done! Your app deploys automatically

**Setup Time:** ~5 minutes

---

### ✅ Option 2: Render.com (Great Alternative)
**Pros:**
- Supports long-running web services
- Free tier available
- Docker support
- Better for Streamlit than Vercel

**Steps:**
1. Create account at [render.com](https://render.com)
2. New → Web Service → Connect GitHub repo
3. Set environment variables including `OPENAI_API_KEY`
4. Deploy

**Setup Time:** ~10 minutes

---

### ✅ Option 3: Railway.app
**Pros:**
- Excellent Streamlit support
- Simple configuration
- Good free tier

**Steps:**
1. Create account at [railway.app](https://railway.app)
2. New Project → GitHub repo
3. Add `OPENAI_API_KEY` environment variable
4. Deploy

**Setup Time:** ~8 minutes

---

## ⚠️ Option 4: Vercel (Not Recommended)

**If you still want to use Vercel:**

### Requirements:
- You need a workaround wrapper or custom API
- Streamlit itself won't work natively
- Consider converting to FastAPI/Flask instead

### Alternative: Use Docker on Vercel
Vercel supports Docker deployments. Create `vercel.json`:

```json
{
  "buildCommand": null,
  "framework": null,
  "functions": {
    "api/**/*.py": {
      "runtime": "python3.11"
    }
  },
  "images": {
    "sizes": [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    "formats": ["image/webp", "image/avif"]
  },
  "env": {
    "OPENAI_API_KEY": "@openai_api_key"
  },
  "regions": ["iad1"]
}
```

But this still won't work well with Streamlit's architecture.

---

## 🚀 Quick Deployment Steps for Streamlit Cloud (Recommended)

### Step 1: Prepare Your Repository
```bash
# Make sure your repo is clean
git add -A
git commit -m "Ready for Streamlit Cloud deployment"
git push origin main
```

### Step 2: Create Streamlit Cloud Account
- Visit: https://share.streamlit.io
- Click "Sign up with GitHub"
- Authorize Streamlit

### Step 3: Deploy Your App
1. Click "New app"
2. Select your repository (Rasikashree/TalentScout-Chatbot)
3. Select branch: `main`
4. Enter app file path: `app.py`
5. Click "Deploy"

### Step 4: Add Secrets
1. Click your profile → Settings
2. Go to "Secrets" section
3. Add:
```
OPENAI_API_KEY=sk-proj-your_key_here
LLM_MODEL=gpt-3.5-turbo
```
4. Save

### Step 5: Access Your App
- Your app is now live at: `https://[username]-[app-name].streamlit.app`
- Auto-redeploys when you push to GitHub

---

## 📋 Checklist Before Deployment

- [ ] `.env` file is in `.gitignore` (don't commit secrets!)
- [ ] `requirements.txt` includes all dependencies
- [ ] App runs locally: `streamlit run app.py`
- [ ] No hardcoded API keys in code
- [ ] All environment variables are documented

---

## 🔐 Security: Handling Secrets

**NEVER commit `.env` file!**

### For Streamlit Cloud:
```bash
# 1. Add to .gitignore
echo ".env" >> .gitignore

# 2. Commit
git add .gitignore
git commit -m "Add .env to .gitignore"
git push

# 3. Add secrets in Streamlit Cloud dashboard
```

### For Render/Railway:
Use their dashboard to set environment variables.

---

## 🆘 Troubleshooting

### "App not loading"
- Check that `app.py` exists in root
- Verify `requirements.txt` has all dependencies
- Check deployment logs for errors

### "API key not working"
- Verify `OPENAI_API_KEY` is set in deployment secrets
- Check secret name matches `os.getenv("OPENAI_API_KEY")`
- Ensure key is valid and has API access

### "Memory/Timeout errors"
- Streamlit Cloud has generous free tier (1GB RAM)
- Consider optimizing your code if using external APIs
- May need paid tier for production use

---

## 💡 Pro Tips

1. **Local testing before deploy:**
   ```bash
   streamlit run app.py
   ```

2. **View deployment logs:**
   - Streamlit Cloud: Dashboard → App settings → Logs
   - Render: Dashboard → Logs tab
   - Railway: Logs tab

3. **Automatic redeploys:**
   - Just push to your repo
   - Streamlit Cloud automatically deploys

4. **Custom domain (if paid):**
   - Streamlit Cloud: Pro plan
   - Render/Railway: Usually included

---

## 📞 Need Help?

- **Streamlit Cloud Docs:** https://docs.streamlit.io/deploy/streamlit-cloud
- **Render Docs:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **Vercel Python Docs:** https://vercel.com/docs/frameworks/python

---

**Bottom Line:** Use **Streamlit Cloud** for best results! It's free, takes 5 minutes, and works perfectly with your app.
