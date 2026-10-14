# Lab 5 — Reflection Questions

## 1. Which issues were easiest and hardest to fix, and why?

The easiest issues were style-related problems such as adding a final newline, removing an unused import, and wrapping a long line. These changes did not require changing the program's logic. The harder issues were the security-related findings, especially removing `eval()` and replacing unsafe shell execution. These required changing how the program handled values and operations while keeping the intended payroll behaviour.

## 2. Did the tools report any false positives? Describe an example.

I did not confirm a definite false positive from the findings reviewed. Most findings identified genuine style, reliability, or security concerns. A tool warning should still be reviewed in context rather than fixed blindly; if a warning is judged to be a false positive, the reason should be documented and the code should be checked carefully.

## 3. How can static analysis tools be integrated into a development workflow?

Run Pylint, Bandit, and Flake8 after making changes and before submitting or committing code. Fix high-risk security findings first, then correctness and maintainability issues, and finally style warnings. The tools can also be run automatically before commits or in continuous integration so new problems are caught early.

## 4. What tangible improvements were observed after fixing the issues?

The revised code uses clearer snake_case naming and docstrings, avoids a mutable list default and dynamic `eval()`, uses SHA-256 instead of MD5, generates tokens with the `secrets` module, and writes files with an explicit UTF-8 encoding and a context manager. In the results previously observed, Bandit reported no issues and Pylint improved from 5.32/10 to 9.80/10. Flake8 still reported a missing final newline at that point, so it must be rerun after saving the newline fix before claiming all checks pass.
