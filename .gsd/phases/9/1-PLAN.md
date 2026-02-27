---
phase: 9
plan: 1
wave: 1
---

# Plan 9.1: Personal Stats API & Wellness Logic

## Objective
Implement a backend API to retrieve a user's own prediction history and compute a "Personal Wellness Score" based on their latest assessments.

## Context
- .gsd/SPEC.md
- backend/main.py (Add endpoint)
- backend/database.py (Add query)

## Tasks

<task type="auto">
  <name>Implement User Stats API</name>
  <files>
    - backend/main.py
    - backend/database.py
  </files>
  <action>
    1. Add `get_user_stats` function to `backend/database.py` that retrieves all records for a specific email.
    2. Add `GET /api/user/stats?email={email}` endpoint to `backend/main.py`.
    3. Ensure the result includes a computed `wellness_score`. 
    Algorithm: 
    - Average of (100 - Risk%) for Heart, Diabetes, and Parkinsons.
    - If an assessment is missing, default that component to 100 (neutral).
  </action>
  <verify>curl "http://localhost:8000/api/user/stats?email=test@example.com"</verify>
  <done>Endpoint returns JSON with prediction history and a wellness_score (0-100).</done>
</task>

<task type="auto">
  <name>Update Data Logging for Consistency</name>
  <files>
    - backend/utils.py
  </files>
  <action>
    Ensure `log_prediction` outcomes are stored in a way that the numerical risk is easily extractable (e.g., "75.0% Risk" should be parsed as 75.0).
  </action>
  <verify>Check database entries for numerical consistency.</verify>
  <done>Outcomes are consistently formatted as "XX.X% Risk".</done>
</task>

## Success Criteria
- [ ] Users can fetch their history via the new API.
- [ ] Wellness score is dynamically calculated based on the latest records for each assessment type.
