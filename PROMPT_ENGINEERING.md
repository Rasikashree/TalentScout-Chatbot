# Prompt Engineering & Design Document

## Overview
This document details the prompt engineering strategy used in TalentScout to create effective interactions with the LLM.

## 1. System Prompt Design

### Purpose
The system prompt defines the personality, role, and boundaries of the assistant.

### Key Elements
```
- Clear Role Definition: "You are TalentScout, an intelligent Hiring Assistant"
- Purpose Statement: Three main goals defined upfront
- Guidelines: Behavioral rules and constraints
- Safety Rails: What NOT to do
```

### Effectiveness Techniques
1. **Role Specification** - Explicit job description for the AI
2. **Boundary Definition** - Clear scope limits
3. **Tone Setting** - Professional yet approachable
4. **Exit Strategy** - Defined ending conditions

## 2. Information Gathering Prompts

### Design Approach
Each information request is crafted to:
- Be specific and unambiguous
- Accept natural language variations
- Provide context for the requested information
- Maintain conversational flow

### Example - Tech Stack Prompt
```
"Could you please list the technologies you are proficient in? 
Please mention programming languages, frameworks, databases, 
and tools you work with. (You can list them separated by commas)"
```

### Why This Works
- ✅ Specific (lists examples of what to include)
- ✅ Flexible (accepts comma-separated format)
- ✅ Clear (explains why we need this info implicitly)
- ✅ Natural (conversational language)

## 3. Technical Question Generation

### Difficulty Calibration
```python
Experience Level → Question Difficulty
Entry-level (0-1 year) → Basic fundamentals
Junior (1-3 years) → Practical application
Mid-level (3-7 years) → Advanced concepts
Senior (7-12 years) → Complex problem-solving
Principal+ (12+ years) → Architecture & decisions
```

### Prompt Structure
```
Input Variables:
- Candidate's tech stack
- Years of experience
- Target position
- Specific technologies to assess

Output Format:
- Ordered list of questions
- Mix of theoretical and practical
- Appropriate difficulty level
```

### Question Types
1. **Conceptual** - "What is the difference between X and Y?"
2. **Practical** - "How would you build X with Y?"
3. **Scenario-based** - "Given X constraint, how would you..."
4. **Best practices** - "What is the best way to handle X?"

## 4. Context Management Prompts

### Problem Addressed
LLMs can lose context in long conversations. Solution: explicit context prompts.

### Strategy
```
1. Maintain conversation history
2. Periodically provide context summaries
3. Include relevant information in each prompt
4. Clear conversation state tracking
```

### Example Usage
```python
messages = [
    SystemMessage(content=base_system_prompt),
    HumanMessage(content=f"Current context: {candidate_info}"),
    HumanMessage(content=user_input),
]
```

## 5. Clarification & Fallback Prompts

### Purpose
Handle unexpected inputs gracefully without breaking the conversation.

### Design Pattern
```
Input: User message that doesn't match question
↓
Analyze input for intent
↓
Generate contextually appropriate response
↓
Gently redirect to conversation
↓
Output: Helpful message that maintains flow
```

### Examples

**Unclear Input**
```
User: "I like pizza"
Response: "That's great! Going back to your professional background, 
how many years have you been working in technology?"
```

**Off-Topic Input**
```
User: "What's the weather?"
Response: "I'm specifically here to help with your hiring assessment. 
Let me refocus: You mentioned playing with Python and React..."
```

## 6. Validation Prompts

### Purpose
Ensure collected information is valid and complete.

### Implementation
```python
# For each field, we validate:
- Format correctness (email regex, phone pattern)
- Completeness (no empty values)
- Reasonableness (0-70 years for experience)
- Clarity (recognizable tech stack items)
```

## 7. Prompt Optimization Techniques

### 1. Specificity
❌ Bad: "Tell me about your experience"
✅ Good: "How many years of professional technology experience do you have?"

### 2. Chunking
❌ Bad: Multiple questions at once
✅ Good: One question per interaction

### 3. Role Playing
```
"You are an expert recruiter assessing..."
"As an AI hiring assistant, your role is..."
```

### 4. Few-Shot Examples
```
"For example, if you specify 'Python, Django, PostgreSQL, Docker', 
I would understand all four technologies."
```

### 5. Explicit Constraints
```
"Do not ask for passwords, financial information, or sensitive data."
"Keep the conversation professional and focused on hiring assessment."
```

## 8. Tone & Voice Guidelines

### Characteristics
- **Professional** - Industry-appropriate language
- **Friendly** - Warm, approachable tone
- **Clear** - Avoid jargon where possible
- **Encouraging** - Positive reinforcement
- **Concise** - Brief responses, no unnecessary fluff

### Brand Voice Example
```
❌ "PROVIDE TECHNICAL COMPETENCIES IMMEDIATELY"
✅ "Could you share the programming languages and frameworks 
   you work with? We'd love to understand your technical background."
```

## 9. Dynamic Prompt Adaptation

### Variables Injected at Runtime
```python
{name} - Candidate's name
{company_name} - Company (TalentScout)
{position} - Target position
{experience_years} - Years of experience
{tech_stack} - Listed technologies
```

### Example
```
Before: "What is your experience with {position}?"
After: "What is your experience with Backend Engineering?"
```

## 10. Error Handling in Prompts

### Fallback Chain
```
1. Try to understand user intent
2. If unclear, ask for clarification
3. If repeated issues, provide examples
4. If still stuck, offer predefined options
5. Last resort: Explain limitation and redirect
```

### Example Prompt
```
"I want to make sure I understand correctly. 
By 'full-stack', do you mean you work with both 
frontend (React, Vue) and backend (Node.js, Python) technologies?"
```

## 11. Cost Optimization

### Token Efficiency
- Avoid unnecessary context repetition
- Use concise prompts
- Batch similar operations
- Clear, direct instructions (fewer tokens)

### Example
```
❌ "In the context of this conversation where we have been 
   discussing various aspects of your professional background, 
   could you elaborate on your understanding of..."
✅ "How do you approach testing in your projects?"
```

## 12. Measuring Prompt Effectiveness

### Metrics
- Question clarity (do candidates understand?)
- Response relevance (do answers match questions?)
- Conversation flow (natural progression?)
- Completion rate (do candidates finish?)
- Time per stage (are we efficient?)

### Evaluation Checklist
- [ ] Prompts are clear without being condescending
- [ ] All information requests are necessary
- [ ] Questions appropriately challenge candidates
- [ ] Tone remains consistent throughout
- [ ] Graceful error handling throughout
- [ ] No prompt injection vulnerabilities

## 13. Advanced Techniques Used

### Chain-of-Thought
```
"Let me think about the best questions to ask based on: 
[Python, Django, PostgreSQL]. 
First, I should assess fundamental Python knowledge...
Then, Django-specific patterns...
Finally, database design with PostgreSQL..."
```

### Few-Shot Learning
```
Example: "If someone says 'I know Node.js and React', 
I understand they can work with JavaScript full-stack development."
```

### Retrieval Augmented Generation
```
When generating questions, the system considers:
- Common technologies and their patterns
- Difficulty-appropriate questions
- Industry best practices
```

## 14. Prompt Versioning & Improvement

### Iteration Process
1. **Baseline** - Test initial prompts
2. **Collection** - Gather user feedback
3. **Analysis** - Identify issues
4. **Refinement** - Update prompts
5. **Testing** - Validate improvements

### Version Control
Each prompt change is tracked with:
- Version number
- Change description
- Testing results
- Approved by (person)

## 15. Security in Prompts

### Prompt Injection Prevention
- Don't concatenate unsanitized user input
- Validate inputs before passing to LLM
- Use clear separators between system and user content
- Avoid instructions like "ignore previous instructions"

### Safe Prompt Structure
```python
messages = [
    SystemMessage(content=SYSTEM_PROMPT),  # Fixed
    HumanMessage(content=categorized_input),  # User input
]
```

## Conclusion

Effective prompt engineering in TalentScout relies on:
1. Clear role definition
2. Specific, unambiguous requests
3. Appropriate context management
4. Graceful error handling
5. Continuous optimization
6. Security-first approach

The prompts are designed to create a hiring experience that is:
- **Professional** - Reflects company standards
- **Inclusive** - Welcomes diverse candidates
- **Efficient** - Respects candidates' time
- **Fair** - Assesses actual skills objectively

---

**Last Updated:** March 2, 2026
**Version:** 1.0
**Author:** TalentScout Development Team
