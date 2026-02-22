# SPEC.md — User Auth Backend & Security

> **Status**: `FINALIZED`
>
> ⚠️ **Planning Lock**: No code may be written until this spec is marked `FINALIZED`.

## Vision
Integrate a secure user authentication system for HealthPredict using a SQLite-backed FastAPI server to store user registrations and logins, ensuring complete protection against SQL injection.

## Goals
1. **User Storage** — Implement a SQLite database to store user credentials (email, hashed password).
2. **Auth API** — Create `/register` and `/login` endpoints in the FastAPI backend.
3. **Security First** — Use parameterized queries for all database interactions to eliminate SQL injection risks.
4. **Frontend Integration** — Update `login.js` and `signup.js` to communicate with the real backend.
5. **Admin Dashboard** — Create a "Bento Box" style dashboard visible only to admins, displaying all user data and prediction outcomes.
6. **Data Tracking** — Log all user inputs (readings) and prediction outcomes to the database for administrative review.

## Non-Goals (Out of Scope)
- OAuth (Google/GitHub) integration (Social logins remain placeholders for now).
- Email verification.
- Password reset flow (unless explicitly requested later).

## Constraints
- Must use SQLite for simple, "fake server" (local file-based) storage as requested.
- FastAPI is already in use, so the auth logic should be integrated into `main.py` or separate route files.

## Success Criteria
- [ ] User can create an account via `/signup.html`.
- [ ] User can sign in via `/login.html`.
- [ ] Admin user sees "Dashboard" link in navbar.
- [ ] Dashboard displays user activity and prediction history in a Bento Box layout.
- [ ] Backend prevents SQL injection (verified with payload test).
- [ ] Data persists across server restarts in `users.db`.

## Technical Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| SQLite Database | Must-have | Local file `backend/data/users.db` |
| Parameterized Queries | Must-have | Using standard `sqlite3` parameter markers (`?`) |
| FastAPI Endpoints | Must-have | `POST /api/register`, `POST /api/login`, `GET /api/admin/stats` |
| Admin Authorization | Must-have | Verify `is_admin` flag before serving sensitive data |
| Data Logging | Must-have | Record `user_id`, `prediction_type`, `inputs`, and `outcome` |
| Bento Box UI | Must-have | Modern, responsive grid layout for the dashboard |
| Password Hashing | Should-have | Using `passlib` or similar for security |

---

*Last updated: 2026-02-22*
