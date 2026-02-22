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
- [ ] Backend prevents SQL injection (verified with payload test).
- [ ] Data persists across server restarts in `users.db`.

## Technical Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| SQLite Database | Must-have | Local file `backend/data/users.db` |
| Parameterized Queries | Must-have | Using standard `sqlite3` parameter markers (`?`) |
| FastAPI Endpoints | Must-have | `POST /api/register` and `POST /api/login` |
| Password Hashing | Should-have | Using `passlib` or similar for security |

---

*Last updated: 2026-02-22*
