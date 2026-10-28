# Software Engineering Lab Submissions — PES1UG24CS327

**Name:** Prahas Bodanapati
**SRN:** PES1UG24CS327
**Section:** 5F

This repository contains my Software Engineering lab work. Labs 1-3 build a single system design, the **Hyperlocal Courier Dispatch & Tracking Engine (Problem Statement #23)**, from requirements to Agile backlog to architecture. Lab 4 is a separate hands-on coding lab (a Python sliding puzzle fixed and extended with an LLM). Lab 5 applies static code analysis (Pylint, Bandit, Flake8) to a Python radio-schedule program.

## Repository Structure

```
.
├── README.md
├── Lab1/   Requirements & use-case modelling
│   ├── Requirements_Table.docx
│   ├── UseCase_diagram.pdf
│   └── UseCase_Flow_RequestCourierPickup.docx
├── Lab2/   Agile backlog & sprint simulation (Jira)
│   ├── Prahas_Bodanapati_PES1UG24CS327_JiraLab2.pdf
│   ├── Jira backlog with Epics and User Stories (1).jpeg
│   ├── Story point assignments (1).jpeg
│   ├── Sprint Board (active sprint view) (1).jpeg
│   └── Burndown chart (1).jpeg
├── Lab3/   Architecture selection & component modelling
│   ├── PES1UG24CS327_Architecture_Justification_Lab3.pdf
│   └── Lab3_Component_Diagram_Clear.pdf
├── Lab4/   VibeCoding: sliding puzzle (Python)
│   ├── README.md
│   ├── main.py
│   ├── game.py
│   ├── puzzle.py
│   ├── requirements.txt
│   ├── before_vid.mov
│   ├── after_vid.mov
│   └── chathistory_SE_lab4.pdf
└── Lab5/   Static code analysis: radio schedule (Python)
    ├── README.md
    ├── radio_schedule.py
    ├── issues.md
    ├── reflection.md
    └── reports/
        ├── before/   pylint_report.txt, bandit_report.txt, flake8_report.txt
        └── after/    pylint_report.txt, bandit_report.txt, flake8_report.txt
```

## Overview

| Lab | Topic | Deliverables |
|-----|-------|--------------|
| 1 | Requirements table and use-case modelling | Requirements table, use-case diagram, use-case flow |
| 2 | Agile backlog creation and sprint simulation | Jira backlog, story points, sprint board, burndown chart, reflection report |
| 3 | Architecture selection and component modelling | Architecture justification, UML component diagram |
| 4 | VibeCoding with an LLM | Fixed and extended sliding puzzle, before/after videos, chat history |
| 5 | Static code analysis (Pylint, Bandit, Flake8) | Cleaned script, issue table, reflection, before/after reports |

---

## Lab 1 — Requirements & Use-Case Modelling

**System:** Hyperlocal Courier Dispatch & Tracking Engine (Smart Cities, Transport & Logistics)
**Actors:** Sender Client, Delivery Rider, Recipient, Payment Gateway

- **Requirements_Table.docx** lists 5 functional and 2 non-functional requirements, each with type, priority, acceptance criteria (pass/fail), and rationale:
  - **FR-001:** Match a courier request with the nearest active rider within 3 km.
  - **FR-002:** Generate a one-time password (OTP) that the recipient must enter before an order is marked delivered.
  - **FR-003:** Compute an optimized stop sequence for riders carrying more than one parcel.
  - **FR-004:** Let the sender view the rider's live location until delivery is confirmed.
  - **FR-005:** Authorize payment before a rider is dispatched.
  - **NFR-001:** Live GPS and status updates reach the sender in under 2 seconds.
  - **NFR-002:** Dispatch and matching service uptime of at least 99.5% during operating hours (6 AM - 11 PM).
- **UseCase_diagram.pdf** is a UML use-case diagram for the courier platform. It shows *Request Courier Pickup* (which `<<include>>`s *Match nearest rider*), *Process Payment*, *Verify delivery via OTP*, and *Track live delivery* (which is extended by *Send delay alert* via `<<extend>>`).
- **UseCase_Flow_RequestCourierPickup.docx** gives the full flow specification for *Request Courier Pickup*: preconditions, success and failure postconditions, the main success scenario, and an alternate flow for when no rider is available within the initial 3 km radius (the search radius expands and the sender can wait, retry, or cancel).

## Lab 2 — Agile Backlog Creation & Sprint Simulation

**Tool:** Jira (project *JiraLab2*, key `JIR`)

The Lab 1 requirements were turned into an Agile backlog with four Epics:

1. Courier Dispatch Management
2. Delivery Tracking & Verification
3. Delivery Route Optimization
4. Payment Processing & Authorization

The Epics contain ten User Stories written in "As a / I want / So that" format, prioritized and estimated with Fibonacci story points (58 points in total). All ten were planned into a single sprint, **JIR Sprint 1 (4-8 September 2026)**.

- **Outcome:** 9 of 10 stories were completed. JIR-11 (estimated delivery time based on the selected route, a low-priority enhancement) was left in To Do when the sprint closed.
- **Estimation:** Complex stories such as route optimization (13 pts) were estimated higher than simple status updates (2 pts). Payment authorization (5 pts) was noted as possibly under-estimated.
- **Burndown:** The chart stayed flat for most of the sprint and dropped sharply at the end, showing work done in large batches instead of steadily.

The report **Prahas_Bodanapati_PES1UG24CS327_JiraLab2.pdf** includes the four Jira screenshots (backlog, story points, sprint board, burndown chart) and answers the four reflection questions. The screenshots are also saved separately as `.jpeg` files.

## Lab 3 — Architecture Selection & Component Modelling

**Chosen architecture:** Microservices

**Justification** (Architecture_Justification_Lab3.pdf):

- **Real-time scalability:** Rider Matching and Live Tracking can scale independently to meet the dispatch window and the under-2-second telemetry requirement.
- **Fault isolation and availability:** A failure in payment or OTP verification does not take down the whole platform, which supports the 99.5% uptime target.
- **Security:** Service boundaries isolate sensitive work. The Payment Service alone talks to the Payment Gateway, and an API Gateway authenticates client requests.
- **Performance:** High-load services get extra instances at peak demand while lightweight order operations scale separately.

**Component diagram** (Lab3_Component_Diagram_Clear.pdf) is a UML component diagram. Inside the microservices boundary are the API Gateway, Order Manager, Payment Service, Rider Matching Service, Live Tracking Service, OTP / Delivery Verification, and the Courier Database. Around it are the Sender Client, Delivery Rider App, Recipient App, Maps / Location Provider, and Payment Gateway. The diagram also lists the Lab 1 requirements it reflects.

---

## Lab 4 — VibeCoding: Sliding Puzzle (Python)

A terminal sliding puzzle, fixed and extended using ChatGPT as a coding assistant. The starter code came from `SETAPESU26/22_sliding_puzzle`.

### How to Run

Requires Python 3.9+ and no third-party packages.

```bash
cd Lab4
python main.py
```

### How to Play

1. Choose a board size: `1` = 3x3, `2` = 4x4, `3` = 5x5.
2. Move the blank space with the keys below. The tile on that side slides into the blank.

| Key | Action |
|-----|--------|
| `W` | Blank moves up |
| `A` | Blank moves left |
| `S` | Blank moves down |
| `D` | Blank moves right |
| `Q` | Quit |

3. Arrange the tiles in order from 1 upward, with the blank in the bottom-right corner. The game then shows your total moves and time and exits.

### Code Overview

| File | Responsibility |
|------|----------------|
| `main.py` | Entry point. Creates `SlidingPuzzle` and calls `run()`. |
| `game.py` | Size menu, board display, input loop, move counter, timer, and win handling. |
| `puzzle.py` | Board generation and scrambling, movement rules, and solved-state check. |

### Tasks Completed

1. **Guaranteed solvable boards.** The original code used `random.shuffle`, which makes roughly half of all boards unsolvable. The board is now built solved and scrambled with `size * size * 20` random legal blank moves, never immediately undoing the previous move. A board that scrambles back to solved is nudged so the game never starts already won.
2. **Complete puzzle lifecycle.** `is_solved()` works for any board size. On a win, the game prints a congratulations message with moves and time, then exits, so no command can change the board afterwards.
3. **Size, timer, and move modes.** 3x3, 4x4, and 5x5 boards with a validated menu. The move counter and timer live in the game session, separate from the board.
4. **Valid-action feedback.** `Puzzle.move()` returns `True` only when a tile actually moves. The move count and "Move successful!" appear only then. Invalid moves print an error and do not change the count.

### Testing

I checked 300 fresh boards for each size (3x3, 4x4, 5x5) with an inversion-parity solvability test, and every board was solvable and none started solved. I also confirmed that invalid directions are rejected and that the game menu re-prompts on bad input. The chat history includes a full `test_puzzle.py` covering board generation, a known solution, impossible moves, move counting, timer behaviour, invalid commands, and quitting.

### Constraints Followed

- All state is kept in memory (no CSV, JSON, SQLite, or other storage).
- No external dependencies.
- The original three-file structure was kept.

### Lab 4 Deliverables

- Gameplay video before changes: `Lab4/before_vid.mov`
- Gameplay video after changes: `Lab4/after_vid.mov`
- Updated code: `Lab4/main.py`, `Lab4/game.py`, `Lab4/puzzle.py`
- Complete LLM chat history: `Lab4/chathistory_SE_lab4.pdf`

* * *

## Lab 5 — Static Code Analysis: Radio Schedule (Python)

The assigned repository (`L5_22_radio_schedule`) contains `radio_schedule.py`, a small programme scheduler for a radio station backed by an in-memory SQLite database. It books show slots, lists morning shows, checks slot timing and removes slots. I analysed it with Pylint, Bandit and Flake8, documented the findings and fixed them, one commit per tool.

### How to Run

Requires Python 3.9+ and no third-party packages.

```
cd Lab5
python radio_schedule.py
```

To re-run the analysis:

```
pip install pylint bandit flake8
pylint radio_schedule.py
bandit -r radio_schedule.py
flake8 radio_schedule.py
```

### Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 2.41/10 | **10.00/10** |
| Bandit | 3 issues (2 Medium, 1 Low) | No issues |
| Flake8 | 4 issues | 0 issues |

### Key Fixes

1. **Removed `eval` (Bandit B307).** `overlapFree()` evaluated a string expression. It is now `overlap_free(start_hour, minutes, next_start_hour)` and does the comparison with numbers, so the broad `except Exception` it needed is gone too.
2. **SQL injection (Bandit B608).** The INSERT was built with `%` string formatting, so a show name like `O'Brien Hour` crashed it. It now uses a parameterised query with `?` placeholders.
3. **Hardcoded password (Bandit B105).** `STUDIO_PASSWORD` is read from an environment variable instead of being committed in source.
4. **Global state and a stale counter (Pylint W0603).** `booked_minutes` was a global that `removeSlot()` never decreased. It is now computed from the table with `SUM(minutes)`, and the database connection is created in `create_schedule()` and passed to each function.
5. **Style and quality.** snake_case names, docstrings, f-strings, wrapped long lines, no one-line `if`, and an `if __name__ == "__main__":` guard.

The full issue table is in `Lab5/issues.md` and the reflection answers are in `Lab5/reflection.md`.

### Lab 5 Deliverables

- Cleaned code: `Lab5/radio_schedule.py`
- Issue table: `Lab5/issues.md`
- Reflection: `Lab5/reflection.md`
- Reports before fixes: `Lab5/reports/before/`
- Reports after fixes: `Lab5/reports/after/`
- Commits: one each for the Bandit, Flake8 and Pylint fixes (see commit history)
