# Vercel Deployment Script for TalentScout Chatbot (Windows)

Write-Host "🚀 TalentScout Chatbot - Vercel Deployment Script"
Write-Host "=================================================="
Write-Host ""

# Check if Vercel CLI is installed
$vercelCheck = Get-Command vercel -ErrorAction SilentlyContinue

if ($null -eq $vercelCheck) {
    Write-Host "❌ Vercel CLI not found. Installing..."
    npm install -g vercel
    Write-Host ""
}

Write-Host "📝 Prerequisites:"
Write-Host "   1. Vercel account (create at vercel.com)"
Write-Host "   2. GitHub account connected to Vercel"
Write-Host "   3. Project pushed to GitHub"

Write-Host ""
Write-Host "🔐 Environment Variables:"
Write-Host "   OPENAI_API_KEY = Your OpenAI API key"
Write-Host "   LLM_MODEL = gpt-3.5-turbo"

Write-Host ""
$confirm = Read-Host "Ready to deploy? (y/n)"

if ($confirm -eq 'y' -or $confirm -eq 'Y') {
    Write-Host ""
    Write-Host "📦 Installing dependencies..."
    pip install -r requirements.txt
    
    Write-Host ""
    Write-Host "🔑 Logging into Vercel..."
    vercel login
    
    Write-Host ""
    Write-Host "🚀 Deploying to production..."
    vercel --prod
    
    Write-Host ""
    Write-Host "✅ Deployment complete!"
    Write-Host "📱 Your app is now live!"
    Write-Host ""
    Write-Host "Visit your deployed app at:"
    Write-Host "https://talentscout-chatbot.vercel.app"
} else {
    Write-Host "Deployment cancelled."
}
