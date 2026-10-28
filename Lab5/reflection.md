# Lab 5 — Reflection

**Name:** Prahas Bodanapati  **SRN:** PES1UG24CS327

### 1. Which issues were the easiest to fix, and which were the hardest? Why?

The easiest were the Flake8 style issues (long lines, the one-line `if`) and the Pylint naming, docstring and f-string warnings. They are mechanical: the report gives the exact line and the fix doesn't change behaviour. The SQL injection fix was also quick once I knew to use `?` placeholders.

The hardest was removing `eval`. Deleting it wasn't enough; I had to work out what the string `"7 + 1 <= 13"` was really checking (whether one slot ends before the next starts) and replace it with a function that takes numbers. The global `booked_minutes` was also harder than it looked, because removing the `global` statement forced me to restructure how the connection and the counter are shared, and in doing that I found a real bug the tools didn't name directly: `removeSlot()` never subtracted the removed minutes.

### 2. Did the static analysis tools report any false positives? If so, describe one example.

Bandit's B105 "hardcoded password" is the closest to a false positive. It is a pattern match on the variable name containing "password", and `STUDIO_PASSWORD` is never actually used anywhere in this program, so there was no real exposure in the running code. It is still worth fixing, since a secret in source control leaks through git history. Pylint's `invalid-name` for `booked_minutes` was also slightly misleading: it treated a mutable counter as a constant and suggested UPPER_CASE, when the real problem was that it was global state at all.

### 3. How would you integrate static analysis tools into your actual software development workflow?

Locally, I would run Flake8 and Pylint through a pre-commit hook (or editor integration) so style and quality problems are caught before code is committed. In CI, a GitHub Actions job would run all three tools on every push and pull request, failing the build if Bandit reports any Medium or High issue, if Flake8 reports anything, or if the Pylint score drops below a threshold such as 9.5. Shared config files (`.pylintrc`, `.flake8`) would keep the whole team on the same rules, and any intentional suppressions (`# nosec`, `# pylint: disable=`) would have to be justified in code review.

### 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Security:** no `eval`, and user-supplied text can no longer change the SQL. A show called `O'Brien Hour` used to crash the insert; now it is stored and listed correctly.
- **Correctness:** booked minutes are computed from the table, so removing a slot updates the total and `morning_shows()` stays accurate.
- **Robustness and reuse:** importing the module no longer runs the demo or opens a database, and each schedule has its own connection, so the functions can be tested in isolation.
- **Readability:** snake_case names, docstrings, f-strings and short lines make the file read like standard Python. Pylint went from 2.41 to 10.00, and Bandit and Flake8 report nothing.
