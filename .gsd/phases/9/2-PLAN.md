---
phase: 9
plan: 2
wave: 1
---

# Plan 9.2: User Health Report Card UI

## Objective
Update the user's dashboard (different from admin dashboard or integrated) to show the Personal Health Report Card.

## Context
- frontend/dashboard.html (or create a separate user_dashboard.html)
- frontend/js/dashboard.js

## Tasks

<task type="auto">
  <name>Create User Health Report Card Section</name>
  <files>
    - frontend/dashboard.html
    - frontend/js/dashboard.js
    - frontend/css/dashboard.css
  </files>
  <action>
    1. If the logged-in user is NOT an admin, hide the admin stats and show a "Your Health Progress" section.
    2. Display the Wellness Score as a large circular gauge or progress bar.
    3. List the 3 assessment types (Heart, Diabetes, Parkinson's) with their latest status (High/Med/Low Risk).
    4. Implement fetch logic in `dashboard.js` to call `/api/user/stats` with the current user's email.
  </action>
  <verify>Login as a regular user and check the dashboard.</verify>
  <done>User sees their own wellness score and assessment history instead of the admin panel.</done>
</task>

## Success Criteria
- [ ] Non-admin users see their "Personal Health Report Card".
- [ ] Wellness score gauge accurately reflects the data from the API.
