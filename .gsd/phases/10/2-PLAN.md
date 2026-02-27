---
phase: 10
plan: 2
wave: 1
---

# Plan 10.2: Symptom Checker UI & Redirection

## Objective
Integrate the AI Symptom Checker into the main frontend and product page.

## Context
- frontend/index.html
- frontend/product.html

## Tasks

<task type="auto">
  <name>Integrate Symptom Checker into Frontend</name>
  <files>
    - frontend/index.html
    - frontend/product.html
    - frontend/about.html
  </files>
  <action>
    1. Add a prominent "Not sure where to start? Try our AI Symptom Checker" card or button on the home and product pages.
    2. Link it to the triage app (port 8505).
    3. Update the navbar to include the Symptom Checker if it adds value.
  </action>
  <verify>Click the Symptom Checker link from the home page.</verify>
  <done>User can easily access the Triage bot from the landing page.</done>
</task>

## Success Criteria
- [ ] Symptom Checker is visible and accessible to new users.
- [ ] Redirection works correctly and passes user context (email/lang).
