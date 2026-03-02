# Contributing to TalentScout

Thank you for your interest in contributing to TalentScout! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help each other learn and grow
- Focus on the code, not the person

## How to Contribute

### 1. Report Issues
- Check if the issue already exists
- Provide clear description
- Include steps to reproduce
- Share your environment details

### 2. Suggest Features
- Describe the feature clearly
- Explain the use case
- Provide examples if applicable
- Consider implementation complexity

### 3. Submit Code Changes

#### Setup Development Environment
```bash
git clone <repository>
cd talentscout_chatbot
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install pytest flake8 black
```

#### Make Changes
1. Create a feature branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test your changes locally
4. Follow code style guidelines (see below)

#### Code Style
```bash
# Format code with Black
black src/ app.py config.py

# Check style with flake8
flake8 src/ app.py --max-line-length=100

# Run tests
python test_chatbot.py
```

#### Commit & Push
```bash
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name
```

#### Create Pull Request
1. Go to GitHub repository
2. Create Pull Request from your feature branch
3. Provide clear description of changes
4. Link related issues
5. Wait for review

### 4. Documentation
- Update README if needed
- Add docstrings to functions
- Include comments for complex logic
- Update changelog

## Development Guidelines

### Code Quality
- Write clean, readable code
- Use meaningful variable names
- Keep functions small and focused
- Add error handling
- Include docstrings (Google style)

### Testing
```python
def function_name(param1, param2):
    """
    Brief description.
    
    Args:
        param1: Description
        param2: Description
    
    Returns:
        Description of return value
    """
    pass
```

### Security
- Never commit API keys or secrets
- Validate all user inputs
- Use environment variables for config
- Follow OWASP guidelines
- Regular dependency updates

### Performance
- Minimize API calls
- Use caching where appropriate
- Avoid redundant operations
- Profile before optimizing

## Project Structure

```
talentscout_chatbot/
├── src/
│   ├── chatbot.py      # Main logic
│   ├── prompts.py      # Prompt templates
│   ├── utils.py        # Utilities
│   └── __init__.py
├── app.py              # Streamlit UI
├── config.py           # Configuration
├── test_chatbot.py     # Tests
└── README.md           # Documentation
```

## Branching Strategy

- `main` - Production-ready code
- `develop` - Development branch
- `feature/*` - Feature branches
- `bugfix/*` - Bug fix branches
- `hotfix/*` - Hotfix branches

## Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

Types: feat, fix, docs, style, refactor, perf, test, chore

Example:
```
feat: Add sentiment analysis to chatbot

Implement sentiment analysis using TextBlob to gauge
candidate emotions during conversation.

Closes #123
```

## Review Process

1. **Code Review** - At least one approval
2. **Testing** - All tests must pass
3. **Documentation** - Update docs as needed
4. **Merge** - Squash and merge to main

## Release Process

1. Update version in `README.md`
2. Update CHANGELOG
3. Tag release: `git tag v1.0.0`
4. Create GitHub release
5. Announce on channels

## Areas for Contribution

### High Priority
- [ ] Multilingual support
- [ ] Sentiment analysis enhancement
- [ ] Advanced analytics dashboard
- [ ] ATS integration

### Medium Priority
- [ ] Video interview support
- [ ] Resume parsing
- [ ] Interview scheduling
- [ ] Email notifications

### Nice to Have
- [ ] Mobile app
- [ ] Custom branding options
- [ ] Advanced reporting
- [ ] Integrations with HR tools

## Getting Help

- Check documentation in README.md
- Review CHALLENGES_SOLUTIONS.md
- Ask in discussions
- Open an issue for questions

## Recognition

Contributors will be recognized in:
- README contributors section
- CONTRIBUTORS.md file
- Release notes

Thank you for contributing to TalentScout! 🚀
