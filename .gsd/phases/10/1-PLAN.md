---
phase: 10
plan: 1
wave: 1
---

# Plan 10.1: Secure Auth (Bcrypt & JWT)

## Objective
Harden the authentication system by implementing industry-standard password hashing and token-based session management. This replaces insecure plain-text storage and simple query parameter identity passing.

## Context
- `backend/main.py`: Contains registration and login logic.
- `backend/database.py`: Handles database schema.
- `frontend/js/login.js`, `frontend/js/signup.js`: Handles auth requests.
- `frontend/js/global.js`: Manages global user state and URL propagation.

## Tasks

<task type="auto">
  <name>Implement Password Hashing</name>
  <files>
    <file>backend/main.py</file>
  </files>
  <action>
    - Install `passlib[bcrypt]`.
    - Update `/api/register` to hash passwords before storing.
    - Update `/api/login` to use `bcrypt.verify` instead of direct comparison.
    - Note: Existing plain-text passwords will need to be handled or reset (for this project, we can clear the `users` table or assume new users only).
  </action>
  <verify>Try registering a new user and confirm the password in `users.db` is a long bcrypt hash.</verify>
  <done>Passwords are stored as hashes and login still works for new users.</done>
</task>

<task type="auto">
  <name>JWT Integration & Session Management</name>
  <files>
    <file>backend/main.py</file>
  </files>
  <action>
    - Install `PyJWT`.
    - Implement a `create_access_token` utility.
    - Update `/api/login` to return a JWT token upon successful auth.
    - Create a middleware or dependency to verify tokens for sensitive routes like `/api/admin/stats`.
  </action>
  <verify>Login should return a `token` in the JSON response.</verify>
  <done>JWT tokens are generated on login and validated on protected endpoints.</done>
</task>

<task type="auto">
  <name>Frontend JWT Adoption</name>
  <files>
    <file>frontend/js/login.js</file>
    <file>frontend/js/global.js</file>
  </files>
  <action>
    - Update `login.js` to store the JWT token in `localStorage`.
    - Refactor `global.js` (`checkAuthState`) to validate users based on token presence/expiry.
    - Update Streamlit URL propagation in `global.js` to pass a short-lived token or use the token to fetch user context securely. (For now, passing the token in query params is still "better" than plain email, but we'll focus on replacing plain email).
  </action>
  <verify>Admin dashboard should still load but use the token for the stats request.</verify>
  <done>Frontend uses JWT for all authenticated requests.</done>
</task>

## Success Criteria
- [ ] No plain-text passwords in `users` table.
- [ ] Login returns a valid JWT.
- [ ] Protected API routes reject requests without a valid token.
