# Lab 5 — Static Code Analysis: Radio Schedule

**Name:** Prahas Bodanapati  **SRN:** PES1UG24CS327  **Section:** 5F

Assigned repository: `L5_22_radio_schedule`. File analysed: `radio_schedule.py`, a programme schedule for a radio station (books slots, lists morning shows, checks timing, removes slots).

## Run

```
python radio_schedule.py
```

Expected output:

```
Sunrise Beats hosted by Vik
True ['Sunrise Beats']
```

## Analysis

```
pip install pylint bandit flake8
pylint radio_schedule.py > pylint_report.txt
bandit -r radio_schedule.py > bandit_report.txt
flake8 radio_schedule.py > flake8_report.txt
```

| Tool | Before | After |
|------|--------|-------|
| Pylint | 2.41/10 | 10.00/10 |
| Bandit | 3 issues (2 Medium, 1 Low) | No issues |
| Flake8 | 4 issues | 0 issues (empty report) |

## Files

- `radio_schedule.py`: cleaned version
- `issues.md`: issue table (type, lines, description, fix)
- `reflection.md`: answers to the reflection questions
- `reports/before/`, `reports/after/`: Pylint, Bandit and Flake8 reports before and after the fixes

## Commits

1. Fix Bandit issues: parameterised SQL (B608), remove `eval` (B307), password from env (B105)
2. Fix Flake8 issues: wrap long lines (E501), split one-line `if` (E701)
3. Fix Pylint issues: snake_case, docstrings, f-strings, remove globals, main guard
