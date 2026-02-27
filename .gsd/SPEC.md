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
7. **Personal Health Report Card** — Aggregate prediction data from all assessments to calculate a "Wellness Score".
8. **Enhanced Medical Bot** — Upgrade the chatbot with a Triage system to direct users to appropriate assessments based on symptoms.
9. **Secure Infrastructure** — Implement password hashing (bcrypt) and JWT-based authentication.
10. **Model Retraining Pipeline** — Create an automated pipeline to improve model accuracy using anonymized user data.

## Non-Goals (Out of Scope)
- OAuth (Google/GitHub) integration (Social logins remain placeholders for now).
- Email verification.
- Password reset flow (unless explicitly requested later).
- Integration with external health trackers (Fitbit/Apple Health).

## Constraints
- Must use SQLite for storage.
- Streamlit apps must communicate with the database via the established logging mechanism.
- AI features must use the existing OpenRouter API setup.

## Success Criteria
- [x] User can create an account via `/signup.html`.
- [x] User can sign in via `/login.html`.
- [x] Admin user sees "Dashboard" link in navbar.
- [x] Dashboard displays user activity and prediction history in a Bento Box layout.
- [x] Backend prevents SQL injection (verified with payload test).
- [x] Data persists across server restarts in `users.db`.
- [ ] Users can see their "Personal Health Report Card" on their profile/dashboard.
- [ ] Medical Bot correctly identifies relevant assessment categories based on natural language input and provides links.

## Technical Requirements

| Requirement | Priority | Notes |
|-------------|----------|-------|
| SQLite Database | Must-have | Local file `backend/data/users.db` |
| Parameterized Queries | Must-have | Using standard `sqlite3` parameter markers (`?`) |
| FastAPI Endpoints | Must-have | `POST /api/register`, `POST /api/login`, `GET /api/admin/stats` |
| Admin Authorization | Must-have | Verify `is_admin` flag before serving sensitive data |
| Data Logging | Must-have | Record `user_id`, `prediction_type`, `inputs`, and `outcome` |
| Bento Box UI | Must-have | Modern, responsive grid layout for the dashboard |
| Triage Logic | Must-have | LLM-based system inside the Medical Bot to map symptoms to Heart/Diabetes/Parkinsons |
| Password Hashing | Must-have | Bcrypt for secure credential storage |
| JWT Authentication| Must-have | Secure sessions instead of plain query parameters |
| Automated Retraining| Should-have | Pipeline for .sav model updates using new data |
| Aggregation Logic | Must-have | Backend logic to calculate wellness score from history |

---

*Last updated: 2026-02-27*
