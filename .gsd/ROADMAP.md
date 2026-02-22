---
milestone: User Authentication & Security
version: 0.1.0
updated: 2026-02-22
---

# Roadmap

> **Current Phase:** 1 - Backend Foundation
> **Status:** 🔄 Planning

## Must-Haves (from SPEC)

- [ ] SQLite database for user storage
- [ ] Parameterized queries to prevent SQLi
- [ ] /register and /login API endpoints
- [ ] Frontend integration with backend API

---

## Phases

### Phase 1: Backend Foundation (SQLite + API Setup)
**Status:** ✅ Complete
**Objective:** Set up the SQLite database and create the initial FastAPI endpoints for auth.
**Requirements:** SQLite, FastAPI integration.

**Plans:**
- [x] Plan 1.1: Database Schema & Connection
- [x] Plan 1.2: Register & Login Logic (Parameterized)

---

### Phase 2: Frontend Integration
**Status:** ✅ Complete
**Objective:** Connect the login and signup forms to the new backend endpoints.
**Requirements:** Update `js/login.js` and `js/signup.js`.

**Plans:**
- [x] Plan 2.1: Signup Form Integration
- [x] Plan 2.2: Login Form Integration

---

### Phase 3: Security Verification
**Status:** ⬜ Not Started
**Objective:** Audit the implementation for SQL injection vulnerabilities and perform UAT.
**Requirements:** SQLi payload testing.

**Plans:**
- [ ] Plan 3.1: Security Audit & SQLi Testing

---

## Progress Summary

| Phase | Status | Plans | Complete |
|-------|--------|-------|----------|
| 1 | ✅ | 2/2 | 100% |
| 2 | ✅ | 2/2 | 100% |
| 3 | ⬜ | 0/1 | 0% |

---

## Timeline

| Phase | Started | Completed | Duration |
|-------|---------|-----------|----------|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |
