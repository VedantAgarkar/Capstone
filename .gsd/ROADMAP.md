---
milestone: User Authentication & Security
version: 0.1.0
updated: 2026-02-22
---

# Roadmap

> **Current Phase:** 1 - Backend Foundation
> **Status:** 🔄 Planning

## Must-Haves (from SPEC)

- [x] Admin infrastructure (is_admin, predictions table)
- [x] Admin Stats API
- [ ] Bento Box Admin Dashboard UI

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
**Status:** ✅ Complete
**Objective:** Audit the implementation for SQL injection vulnerabilities and perform UAT.
**Requirements:** SQLi payload testing.

**Plans:**
- [x] Plan 3.1: Security Audit & SQLi Testing

---

## Progress Summary

| Phase | Status | Plans | Complete |
|-------|--------|-------|----------|
| 1 | ✅ | 2/2 | 100% |
| 2 | ✅ | 2/2 | 100% |
| 3 | ✅ | 1/1 | 100% |
| 4 | ✅ | 2/2 | 100% |
| 5 | ⬜ | 0/2 | 0% |

---

### Phase 4: Admin Infrastructure & Backend
**Status:** ✅ Complete
**Objective:** Evolve the database schema to support admin roles and data tracking.
**Requirements:** `is_admin` column, `predictions` table, stats API.

**Plans:**
- [x] Plan 4.1: Schema Update & Admin Creation
- [x] Plan 4.2: Admin Stats API

---

### Phase 5: Bento Box Admin Dashboard
**Status:** ⬜ Not Started
**Objective:** Create a premium Bento Box style dashboard for admins.
**Requirements:** `dashboard.html`, `dashboard.js`, conditional navbar link.

**Plans:**
- [ ] Plan 5.1: Conditional Dashboard Navigation
- [ ] Plan 5.2: Bento Box UI Implementation

---

## Timeline

| Phase | Started | Completed | Duration |
|-------|---------|-----------|----------|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |
