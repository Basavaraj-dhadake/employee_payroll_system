# Static Code Analysis: Issues and Fixes

> Line numbers below refer to the original version of `employee_payroll_system.py`. Verify or update them against your own original file if it differs.

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| Missing final newline | Style (Pylint/Flake8) | 73 | The source file did not end with a newline. | Added a newline at the end of the file. |
| Missing function docstrings | Maintainability (Pylint) | Multiple | Functions did not explain their purpose. | Added concise docstrings. |
| `processSalary` naming | Style (Pylint) | Function definition | CamelCase function name did not follow snake_case convention. | Renamed it to `process_salary`. |
| Mutable default argument `[]` | Correctness/maintainability (Pylint) | Function definition | A shared list default can retain data across calls. | Used `None`, then created a new list inside the function. |
| Bare `except` / ignored error | Reliability/security (Pylint/Bandit/Flake8) | 26 | Broad exception handling can hide failures. | Removed the broad exception and validate expected inputs explicitly. |
| `== None` comparison | Style (Pylint/Flake8) | 32 | Explicit equality comparison with `None` is discouraged. | Used `is None` where needed. |
| Unused variables/import | Style (Pylint/Flake8) | 6, 31, 41 | Unused names make code harder to maintain. | Removed the unused `math` import and unused variables. |
| `eval()` | Security (Bandit) | 42 | Evaluating a string as code can execute unintended expressions. | Removed dynamic evaluation and used a configured numeric tax rate. |
| MD5 hashing | Security (Bandit) | 47 | MD5 is not suitable where a stronger digest is required. | Replaced MD5 with SHA-256. |
| Non-cryptographic random token | Security (Bandit) | 51 | `random.randint` is not designed for security-sensitive tokens. | Used `secrets.token_hex`. |
| Shell execution with `os.system` | Security (Bandit) | 58 | Shell commands can introduce command-injection risk. | Removed shell execution; file export uses Python file I/O. |
| File opened without explicit encoding / manual close | Reliability (Pylint) | File export section | Default encoding can vary and manual close can be skipped after errors. | Used `with open(..., encoding="utf-8")`. |
| Long source line | Style (Flake8) | 19 | A line exceeded the configured line-length limit. | Wrapped long expressions across lines. |

## Summary

The updated program addresses the findings above by improving naming, documentation, input validation, file handling, and security-sensitive operations. Run Pylint, Bandit, and Flake8 on the final saved file and paste their actual outputs into the `after_*` and final report files. Do not report a clean result unless the tools confirm it.
