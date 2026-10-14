"""A small employee payroll system demonstrating safer coding practices."""

import hashlib
import secrets


EMPLOYEES = {
    "EMP101": {"name": "David", "base_salary": 4500.0, "tax_rate": 0.15},
    "EMP102": {"name": "Elena", "base_salary": 5200.0, "tax_rate": 0.20},
    "EMP103": {"name": "Frank", "base_salary": 3800.0, "tax_rate": 0.12},
}


def process_salary(emp_id, bonus, transaction_logs=None):
    """Calculate and return an employee's gross salary."""
    if emp_id not in EMPLOYEES:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    if bonus < 0:
        raise ValueError("Bonus cannot be negative.")

    if transaction_logs is None:
        transaction_logs = []

    employee = EMPLOYEES[emp_id]
    gross_salary = employee["base_salary"] + bonus
    transaction_logs.append(
        f"{emp_id}: gross salary calculated as {gross_salary:.2f}"
    )
    return gross_salary


def deduct_penalty(emp_id, penalty):
    """Return the employee's salary after applying a penalty."""
    if emp_id not in EMPLOYEES:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    if penalty < 0:
        raise ValueError("Penalty cannot be negative.")

    return max(0.0, EMPLOYEES[emp_id]["base_salary"] - penalty)


def check_bonus_eligibility(emp_id, performance_score):
    """Check whether an employee qualifies for a performance bonus."""
    if emp_id not in EMPLOYEES:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    return performance_score >= 80


def compute_net_salary(emp_id, gross_salary):
    """Calculate net salary using the employee's configured tax rate."""
    if emp_id not in EMPLOYEES:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    if gross_salary < 0:
        raise ValueError("Gross salary cannot be negative.")

    tax_rate = EMPLOYEES[emp_id]["tax_rate"]
    return gross_salary * (1 - tax_rate)


def hash_employee_id(emp_id):
    """Return a SHA-256 digest of an employee ID."""
    if emp_id not in EMPLOYEES:
        raise ValueError(f"Unknown employee ID: {emp_id}")
    return hashlib.sha256(emp_id.encode("utf-8")).hexdigest()


def generate_transaction_token():
    """Generate a cryptographically secure transaction token."""
    return secrets.token_hex(16)


def export_payroll_sheet(filename, rows):
    """Write payroll rows to a UTF-8 encoded text file."""
    with open(filename, "w", encoding="utf-8") as payroll_file:
        payroll_file.write("Employee ID,Name,Net Salary\n")
        for emp_id, name, net_salary in rows:
            payroll_file.write(f"{emp_id},{name},{net_salary:.2f}\n")


def main():
    """Run a sample payroll calculation and export the result."""
    employee_id = "EMP101"
    bonus = 350.0
    penalty = 100.0

    gross_salary = process_salary(employee_id, bonus)
    salary_after_penalty = deduct_penalty(employee_id, penalty)
    bonus_eligible = check_bonus_eligibility(employee_id, 85)
    net_salary = compute_net_salary(employee_id, gross_salary)
    employee_hash = hash_employee_id(employee_id)
    transaction_token = generate_transaction_token()

    print(f"Employee: {EMPLOYEES[employee_id]['name']}")
    print(f"Gross salary: {gross_salary:.2f}")
    print(
        "Salary after penalty (separate example): "
        f"{salary_after_penalty:.2f}"
    )
    print(f"Bonus eligible: {bonus_eligible}")
    print(f"Net salary: {net_salary:.2f}")
    print(f"Employee ID SHA-256: {employee_hash}")
    print(f"Transaction token: {transaction_token}")

    export_payroll_sheet(
        "payroll_export.csv",
        [(employee_id, EMPLOYEES[employee_id]["name"], net_salary)],
    )
    print("Payroll exported to payroll_export.csv")


if __name__ == "__main__":
    main()