---
phase: 10
plan: 1
wave: 1
---

# Plan 10.1: Triage Bot Implementation

## Objective
Implement an AI-powered symptom triage bot that analyzes user symptoms and directs them to the specific assessment (Heart, Diabetes, or Parkinson's).

## Context
- backend/utils.py
- backend/main.py
- backend/routes/triage.py (New File)

## Tasks

<task type="auto">
  <name>Create Triage logic</name>
  <files>
    - backend/routes/triage.py
    - backend/main.py
  </files>
  <action>
    1. Create `backend/routes/triage.py` using Streamlit.
    2. Define a specialized system prompt for the Triage Bot.
    3. The bot should identify symptoms related to:
       - Heart (chest pain, shortness of breath)
       - Diabetes (thirst, frequent urination, fatigue)
       - Parkinson's (tremors, stiffness, voice changes)
    4. Provide direct links to the relevant apps within the chat response.
    5. Register the route in `main.py` (port 8505).
  </action>
  <verify>Access http://localhost:8505 and test symptom inputs.</verify>
  <done>Bot correctly suggests Heart assessment for "chest pain" and Parkinson's for "shaking hands".</done>
</task>

## Success Criteria
- [ ] Triage bot identifies symptoms and maps them to one of the 3 assessments.
- [ ] Bot provides a clickable link to the suggested assessment.
