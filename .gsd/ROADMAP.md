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
- [x] Bento Box Admin Dashboard UI

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
| 5 | ✅ | 2/2 | 100% |

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
**Status:** ✅ Complete
**Objective:** Create a premium Bento Box style dashboard for admins.
**Requirements:** `dashboard.html`, `dashboard.js`, conditional navbar link.

**Plans:**
- [x] Plan 5.1: Conditional Dashboard Navigation
- [x] Plan 5.2: Bento Box UI Implementation

---

## Timeline

| Phase | Started | Completed | Duration |
|-------|---------|-----------|----------|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |

---

### Phase 6: Theme Unification
**Status:** ✅ Complete
**Objective:** Update the UI of Dashboard, Login, and Signup pages to match the primary navy blue, gold, and white theme.
**Requirements:** Modify CSS files (`dashboard.css`, `login.css`, inline styles) to use `global.css` CSS variables or exact hex codes. Make the elements blend well.

**Plans:**
- [x] Plan 6.1: Theme Dashboard UI
- [x] Plan 6.2: Theme Login & Signup Pages

---

### Phase 7: Dashboard Data Fix & Refresh Feature
**Status:** ✅ Complete
**Objective:** Fix the missing prediction logging in Streamlit apps to populate the admin dashboard and add a refresh button to the UI.
**Requirements:** Bridge Streamlit apps with the SQLite database, pass user context (email) via query params, and enhance the Dashboard UI.

**Plans:**
- [x] Plan 7.1: Data Logging Infrastructure
- [x] Plan 7.2: Implement Logging in Health Routes
- [x] Plan 7.3: Dashboard Refresh & Final Polish
- [x] Plan 7.4: Robust Identity Tracking & Bot Logging
- [x] Plan 7.5: Fix Marathi PDF Rendering (Wrapping Issue)
- [x] Plan 7.6: Fix Model Warnings & Feature Mismatches (Cleanup)

---

### Phase 8: Multi-Language Support for Streamlit Apps
**Status:** ✅ Complete
**Objective:** Ensure the language selection from the homepage (English/Marathi) persists in the Streamlit assessment apps and chatbot.
**Requirements:** Implementation of translation dictionaries in all Streamlit routes and UI updates based on the 'lang' query parameter.

**Plans:**
- [x] Plan 8.1: Localize Heart Disease Assessment
- [x] Plan 8.2: Localize Parkinson's Disease Assessment
- [x] Plan 8.3: Localize Medical AI Bot & Final Polish

---

### Phase 9: Unified Health Dashboard (Wellness API)
**Status:** ✅ Complete
**Objective:** Develop the logic and UI for the "Personal Health Report Card" to aggregate user data and calculate wellness scores.
**Requirements:** New API endpoint for personal stats, wellness score algorithm, and UI updates for the user dashboard.

**Plans:**
- [x] Plan 9.1: Personal Stats API & Wellness Logic
- [x] Plan 9.2: User Health Report Card UI

---

### Phase 10: AI Symptom Checker (Triage)
**Status:** 🔄 Planning
**Objective:** Implement a dedicated chat interface for symptom triage using LLMs.
**Requirements:** New route for triage bot, mapping logic to health assessments, and frontend integration.

**Plans:**
- [ ] Plan 10.1: Triage Bot Implementation
- [ ] Plan 10.2: Symptom Checker UI & Redirection

---
