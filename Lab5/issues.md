# Lab 5 — Issue Table (radio_schedule.py)

**Name:** Prahas Bodanapati  **SRN:** PES1UG24CS327

Line numbers refer to the original file. Ordered by severity (high/medium first).

| # | Issue | Tool / Code | Type | Severity | Line(s) | Description | Fix Approach |
|---|-------|-------------|------|----------|---------|-------------|--------------|
| 1 | Use of `eval` | Bandit B307, Pylint W0123 | Security | Medium (High confidence) | 21 | `overlapFree()` ran `eval(formula)` on a string, which can execute arbitrary code if the string ever comes from outside. | Removed `eval`. The function now takes numbers `(start_hour, minutes, next_start_hour)` and returns `start_hour*60 + minutes <= next_start_hour*60`. |
| 2 | SQL injection | Bandit B608, Pylint C0209 | Security | Medium | 11 | `addSlot()` built the INSERT with `%` string formatting, so a show name like `O'Brien Hour` breaks the query and crafted input could inject SQL. | Used a parameterised query with `?` placeholders and passed values as a tuple. |
| 3 | Broad exception | Pylint W0718 | Bug / Quality | Medium | 22 | `except Exception: return False` hid every error, including real bugs, and made a failure look like "overlap". | The risky `eval` is gone, so the `try/except` was removed entirely; the function can no longer raise for valid numbers. |
| 4 | Hardcoded password | Bandit B105 | Security | Low | 5 | `STUDIO_PASSWORD = "onair2024"` committed a secret into source control. | Read it from the environment: `os.environ.get("STUDIO_PASSWORD")`. |
| 5 | Global mutable state + stale counter | Pylint W0603, C0103 | Bug / Design | Medium | 6, 10, 12, 31–32 | `booked_minutes` was a module global updated with `global`; `removeSlot()` never decreased it, so it drifted out of sync with the table. The DB connection was also created at import time. | Removed the global. `booked_minutes(conn)` now computes `SUM(minutes)` from the table, and the connection is created in `create_schedule()` and passed to each function. |
| 6 | Code runs on import | Pylint (design) | Bug | Low | 43 | `main()` was called at module level, so importing the file ran the demo. | Wrapped in `if __name__ == "__main__":`. |
| 7 | Naming convention | Pylint C0103 | Style | Low | 9, 15, 19, 26, 31 | camelCase function names (`addSlot`, `slotLabel`, …) break PEP 8. | Renamed to snake_case (`add_slot`, `slot_label`, `overlap_free`, `morning_shows`, `remove_slot`). |
| 8 | Missing docstrings | Pylint C0114, C0116 | Style | Low | 1, 9–35 | No module or function docstrings. | Added a module docstring and one per function. |
| 9 | Old-style formatting | Pylint C0209 | Style | Low | 16 | `"{} hosted by {}".format(...)` | Replaced with an f-string. |
| 10 | Line too long | Flake8 E501, Pylint C0301 | Style | Low | 4, 11, 27 | Lines of 110–135 characters. | Split SQL strings with implicit concatenation and wrapped call arguments. |
| 11 | Multiple statements on one line | Flake8 E701, Pylint C0321 | Style | Low | 27 | `if booked_minutes > 0: return [...]` on one line. | Moved the body onto its own indented lines. |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 2.41/10 (22 messages) | **10.00/10** |
| Bandit | 3 issues (2 Medium, 1 Low) | No issues identified |
| Flake8 | 4 issues | 0 issues (empty report) |

Program output is unchanged before and after:

```
Sunrise Beats hosted by Vik
True ['Sunrise Beats']
```
