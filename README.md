# Lab 5: Static Code Analysis – Employee Payroll System

## 1. Project Overview

This project demonstrates static code analysis and code quality improvement
using Pylint, Bandit, and Flake8 on a Python employee payroll system.

The main objective is to identify and fix code quality, coding style,
maintainability, and security issues.

## 2. Objectives

- Identify code quality issues using Pylint.
- Detect potential security vulnerabilities using Bandit.
- Check coding style and formatting using Flake8.
- Improve code readability and maintainability.
- Compare analysis results before and after fixing issues.

## 3. Tools Used

| Tool | Purpose |
|---|---|
| Pylint | Checks Python code quality and reports a quality score |
| Bandit | Identifies potential security issues |
| Flake8 | Checks Python coding style and formatting |
| Python | Programming language |
| Visual Studio Code | Development environment |
| Git and GitHub | Version control and project hosting |

## 4. Project Structure

```text
L5_44_employee_payroll_system-main/
├── employee_payroll_system.py
├── issues.md
├── reflection.md
├── before_pylint_report.txt
├── before_bandit_report.txt
├── before_flake8_report.txt
├── after_pylint_report.txt
├── after_bandit_report.txt
├── after_flake8_report.txt
├── pylint_report.txt
├── bandit_report.txt
└── flake8_report.txt
```

## 5. Issues Identified and Fixes

The original program contained several code quality and security issues.

Examples include:

- Missing function docstrings.
- Incorrect function naming conventions.
- Mutable default arguments.
- Broad exception handling.
- Unnecessary imports and variables.
- Use of `eval()`.
- Use of MD5 hashing.
- Insecure random token generation.
- Shell command execution.
- File handling and formatting issues.

The fixes and explanations are documented in `issues.md`.

## 6. Improvements Made

- Added function docstrings.
- Improved function naming conventions.
- Replaced mutable default arguments with `None`.
- Added input validation.
- Removed dynamic `eval()` usage.
- Replaced MD5 with SHA-256.
- Used Python's `secrets` module for token generation.
- Removed shell execution using `os.system()`.
- Improved file handling with UTF-8 encoding and a context manager.
- Corrected formatting and line-length issues.

## 7. Running the Project

Make sure Python and the analysis tools are installed.

Install the tools:

```bash
python -m pip install pylint bandit flake8
```

Run the payroll program:

```bash
python employee_payroll_system.py
```

Run Pylint:

```bash
python -m pylint employee_payroll_system.py
```

Run Bandit:

```bash
python -m bandit -r employee_payroll_system.py
```

Run Flake8:

```bash
python -m flake8 employee_payroll_system.py
```

## 8. Analysis Results

The latest confirmed results recorded during development were:

| Tool | Result |
|---|---|
| Pylint | 10.00/10 |
| Bandit | No issues identified |
| Flake8 | Final clean result must be verified |

Run all three tools again after the final code changes and record their
actual outputs in the corresponding report files.

The before-and-after reports document the changes observed during analysis.

## 9. Reflection

The reflection questions and answers are available in `reflection.md`.

## 10. References

- Pylint: https://pylint.readthedocs.io/
- Bandit: https://bandit.readthedocs.io/
- Flake8: https://flake8.pycqa.org/
- CWE-703: https://cwe.mitre.org/data/definitions/703.html
- CWE-78: https://cwe.mitre.org/data/definitions/78.html
- Bandit B110: https://bandit.readthedocs.io/en/1.9.4/plugins/b110_try_except_pass.html

## 11. Conclusion

This lab demonstrates how static analysis tools can improve Python code
quality, maintainability, formatting, and security.

Using Pylint, Bandit, and Flake8 helps developers identify potential
problems before the software is deployed.
