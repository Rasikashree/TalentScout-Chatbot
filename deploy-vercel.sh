#!/bin/bash
# Vercel Deployment Script for TalentScout Chatbot

echo "🚀 TalentScout Chatbot - Vercel Deployment Script"
echo "=================================================="

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
fi

echo ""
echo "📝 Prerequisites:"
echo "   1. Vercel account (create at vercel.com)"
echo "   2. GitHub account connected to Vercel"
echo "   3. Project pushed to GitHub"

echo ""
echo "🔐 Environment Variables:"
echo "   OPENAI_API_KEY = Your OpenAI API key"
echo "   LLM_MODEL = gpt-3.5-turbo"

echo ""
read -p "Ready to deploy? (y/n) " -n 1 -r
echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    
    echo ""
    echo "🔑 Logging into Vercel..."
    vercel login
    
    echo ""
    echo "🚀 Deploying to production..."
    vercel --prod
    
    echo ""
    echo "✅ Deployment complete!"
    echo "📱 Your app is now live!"
else
    echo "Deployment cancelled."
fi
