# Deployment Guide for TalentScout

## Quick Start - Local Deployment

### Prerequisites
- Python 3.8+
- OpenAI API key
- pip

### Steps
```bash
# 1. Clone repository
git clone <repo-url>
cd talentscout_chatbot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# 5. Run application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

---

## Docker Deployment

### Build Docker Image
```bash
# Build the image
docker build -t talentscout:latest .

# Run the container
docker run -p 8501:8501 \
  -e OPENAI_API_KEY=your_key_here \
  -v $(pwd)/data:/app/data \
  talentscout:latest
```

### Using Docker Compose
```bash
# Set up environment variables
cp .env.example .env
# Edit .env with your API key

# Start services
docker-compose up -d

# View logs
docker-compose logs -f talentscout

# Stop services
docker-compose down
```

---

## Cloud Deployment Options

### Option 1: Streamlit Cloud (Easiest)

**Benefits:**
- One-click deployment
- Free tier available
- Automatic updates from GitHub
- Built-in SSL/TLS

**Steps:**
1. Push code to GitHub
2. Visit [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app"
4. Select repository and branch
5. Set environment variables (OPENAI_API_KEY)
6. Deploy

**Cost:** Free tier limited, paid plans available

---

### Option 2: Google Cloud Run

**Benefits:**
- Serverless (no infrastructure management)
- Pay-per-use pricing
- Auto-scaling
- Easy deployment

**Steps:**

```bash
# 1. Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# 2. Authenticate
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# 3. Build and push to Container Registry
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/talentscout

# 4. Deploy to Cloud Run
gcloud run deploy talentscout \
  --image gcr.io/YOUR_PROJECT_ID/talentscout \
  --platform managed \
  --region us-central1 \
  --set-env-vars OPENAI_API_KEY=your_key_here \
  --allow-unauthenticated
```

**Cost:** Free tier (2M requests/month), then $0.24-0.40 per million invocations

---

### Option 3: AWS Lambda + API Gateway

**Benefits:**
- Serverless
- Excellent scalability
- AWS ecosystem integration
- Cost-effective

**Setup:**
```bash
# 1. Install AWS CLI and configure
aws configure

# 2. Use Zappa for easy deployment
pip install zappa

# 3. Initialize Zappa
zappa init

# 4. Deploy
zappa deploy production

# 5. Updates
zappa update production
```

**Note:** Streamlit requires WebSocket support, use Zappa asynchronous mode or consider Lambda + RDS combination.

---

### Option 4: Azure App Service

**Benefits:**
- Enterprise-grade
- Integrated with AD
- Hybrid capabilities
- Good free tier

**Steps:**

```bash
# 1. Create resource group
az group create --name talentscout-rg --location eastus

# 2. Create App Service plan
az appservice plan create \
  --name talentscout-plan \
  --resource-group talentscout-rg \
  --sku B1 \
  --is-linux

# 3. Create web app
az webapp create \
  --resource-group talentscout-rg \
  --plan talentscout-plan \
  --name talentscout-app \
  --runtime "PYTHON|3.11"

# 4. Configure deployment from Git
az webapp up \
  --resource-group talentscout-rg \
  --name talentscout-app \
  --runtime "PYTHON:3.11"

# 5. Set environment variables
az webapp config appsettings set \
  --resource-group talentscout-rg \
  --name talentscout-app \
  --settings OPENAI_API_KEY=your_key_here
```

---

### Option 5: AWS Elastic Beanstalk

**Benefits:**
- Easy deployment
- Environment management
- Auto-scaling
- Good for traditional apps

**Steps:**

```bash
# 1. Install EB CLI
pip install awsebcli

# 2. Initialize application
eb init -p python-3.11 talentscout --region us-east-1

# 3. Create environment
eb create production

# 4. Set environment variables
eb setenv OPENAI_API_KEY=your_key_here

# 5. Deploy
eb deploy

# 6. Monitor
eb health
eb status
```

---

## Environment Variables Setup

### For Cloud Deployments

1. **Streamlit Cloud**
   - Settings → Secrets Management
   - Add: `OPENAI_API_KEY = "your_key"`

2. **Google Cloud Run**
   - Use `--set-env-vars` flag or
   - Cloud Console → Service → Edit & Deploy

3. **Azure App Service**
   - Portal → Configuration → Application settings
   - Add the key-value pair

4. **AWS Services**
   - Systems Manager → Parameter Store
   - Or directly in environment setup commands

---

## Monitoring & Logging

### Local Development
```bash
# Enable debug logging
streamlit run app.py --logger.level=debug
```

### Cloud Monitoring

#### Google Cloud Run
```bash
gcloud run services describe talentscout --region us-central1

# View logs
gcloud logging read "resource.type=cloud_run_revision" \
  --limit 50 \
  --format json
```

#### Azure
```bash
# Tail logs
az webapp log tail --name talentscout-app --resource-group talentscout-rg

# Stream logs
az webapp log stream --name talentscout-app --resource-group talentscout-rg
```

#### AWS Elastic Beanstalk
```bash
eb logs
eb ssh  # SSH into instance
```

---

## Security Best Practices

### 1. API Key Management
- Never commit `.env` to Git
- Use cloud provider's secrets management
- Rotate keys regularly
- Use restricted API keys (IP whitelist, rate limits)

### 2. Network Security
- Use HTTPS (provided by cloud platforms)
- Consider WAF (Web Application Firewall)
- Enable CORS appropriately
- Rate limiting on API calls

### 3. Data Protection
```python
# Ensure data is anonymized
# Implement encryption at rest
# Use secure data transmission
```

### 4. Access Control
- Restrict who can view/modify deployment
- Use IAM roles appropriately
- Enable audit logging
- Regular security audits

---

## Scaling Considerations

### Vertical Scaling (Upgrade machine)
- Increase memory/CPU
- Better for: Single-user LLM models
- Cost: Linear increase

### Horizontal Scaling (More instances)
- Load balancer distributes traffic
- Better for: Multiple concurrent users
- Cost: More predictable

### Caching Layer
```python
# Add Redis for session caching
# Reduces API calls
# Improves response time
```

---

## Performance Optimization

### 1. Reduce API Calls
- Cache tech stack database
- Batch question generation
- Reuse conversation context

### 2. Streamlit Optimization
```python
@st.cache_resource
def get_chatbot():
    return TalentScoutChatbot()

@st.cache_data
def get_tech_database():
    return load_tech_stack_data()
```

### 3. Model Selection
- Use gpt-3.5-turbo for speed
- Use gpt-4 for quality (slower)
- Monitor token usage

---

## Cost Estimation

### Monthly Costs (Estimate)

| Component | Free Tier | Typical | Heavy Use |
|-----------|-----------|---------|-----------|
| App Hosting | $0 | $10-50 | $100+ |
| OpenAI API | - | $5-20 | $50+ |
| Database | $0 | $0-10 | $50+ |
| **Total** | **~$0** | **$15-80** | **$150+** |

### Cost Optimization Tips
1. Use gpt-3.5-turbo (cheaper than gpt-4)
2. Optimize prompts to use fewer tokens
3. Implement caching
4. Monitor API usage
5. Set budget alerts

---

## Troubleshooting Deployment

### Issue: "Module not found"
```bash
# Solution: Ensure all dependencies installed
pip install -r requirements.txt
# Check Python version
python --version  # Should be 3.8+
```

### Issue: "API Key not working"
```bash
# Verify key format
# Check if key has expired
# Ensure environment variable is set
env | grep OPENAI_API_KEY
```

### Issue: "Port already in use"
```bash
# Local: Use different port
streamlit run app.py --server.port 8502

# Docker: Change port mapping
docker run -p 8502:8501 talentscout:latest
```

### Issue: "Slow responses"
```
- Check API rate limits
- Monitor token usage
- Consider model optimization
- Implement caching
- Use load testing to identify bottleneck
```

---

## Rollback Procedures

### Streamlit Cloud
- Navigate to "Recent Commits"
- Select previous version
- It automatically deploys

### Docker/Kubernetes
```bash
# Tag previous image
docker tag talentscout:v1.0.0 talentscout:latest

# Redeploy
docker run ... talentscout:latest
```

### Cloud Platforms
```bash
# Google Cloud Run
gcloud run deploy talentscout --image=[previous-image] ...

# Azure
az webapp deployment slot swap ...

# AWS EB
eb swap
```

---

## Health Checks & Monitoring

### Endpoint Health
```bash
# Check if app is running
curl http://localhost:8501/_stcore/health

# Check API connectivity
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Metrics to Monitor
- Response time
- API error rate
- Token usage
- User completion rate
- Infrastructure resource usage

---

## Maintenance Schedule

**Weekly:**
- Monitor logs for errors
- Check API usage
- Review cost metrics

**Monthly:**
- Update dependencies
- Review security patches
- Analyze performance metrics

**Quarterly:**
- Security audit
- Performance optimization
- Feature review

---

**Last Updated:** March 2, 2026
**Version:** 1.0
