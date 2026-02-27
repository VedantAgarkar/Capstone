---
phase: 10
plan: 2
wave: 1
---

# Plan 10.2: Automated Model Retraining Pipeline

## Objective
Implement a pipeline that improves prediction accuracy over time by enabling models to learn from anonymized user data accumulated in the platform.

## Context
- `backend/train_heart_model.ipynb`: Reference training logic for Heart.
- `backend/train_diabetes_model.ipynb`: Reference training logic for Diabetes.
- `backend/train_parkinsons_model.ipynb`: Reference training logic for Parkinson's.
- `backend/database.py`: Access to historical `predictions` data.

## Tasks

<task type="auto">
  <name>Retraining Utility Implementation</name>
  <files>
    <file>backend/retrain_utils.py</file>
  </files>
  <action>
    - Extract training logic from notebooks into three clean Python functions: `retrain_heart()`, `retrain_diabetes()`, `retrain_parkinsons()`.
    - Implement a data loading layer that:
      1. Loads original baseline CSVs (`heart.csv`, etc.).
      2. Queries the `predictions` table for new records.
      3. Anonymizes the data (removes user IDs).
      4. Merges and formats data to match model expectations.
    - Save updated `.sav` files to their respective locations.
  </action>
  <verify>Run the script and check if the file modification timestamps for `.sav` files are updated.</verify>
  <done>Python-based retraining logic exists for all three models.</done>
</task>

<task type="auto">
  <name>Retraining API & Admin Trigger</name>
  <files>
    <file>backend/main.py</file>
    <file>frontend/js/dashboard.js</file>
  </files>
  <action>
    - Add a `POST /api/admin/retrain` endpoint (JWT protected).
    - This endpoint should trigger the retraining process asynchronously.
    - Add a "Retrain Models" button in the Admin Dashboard UI.
  </action>
  <verify>Clicking the button should return a success message and update the models.</verify>
  <done>Admins can trigger model improvements with a single click.</done>
</task>

## Success Criteria
- [ ] Models can be retrained without manual notebook execution.
- [ ] New data from the database is successfully incorporated into the training set.
- [ ] Retraining can be triggered from the Admin Dashboard.
