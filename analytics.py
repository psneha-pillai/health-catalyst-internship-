'''File: analytics.py

Function: calculate_pay(hours, rate)

Return total pay.

Function: employee_statistics(hours_list)

Return max, min, and average hours.

Function: search_employee(employees, emp_id)

Return employee details if found, otherwise ""Employee not found"".

'''
def calculate_pay(hours, rate):
    return hours * rate
def employee_statistics(hours_list):
    max_hours = max(hours_list)
    min_hours = min(hours_list)
    avg_hours = sum(hours_list) / len(hours_list)
    return max_hours, min_hours, avg_hours
def search_employee(employees, emp_id):
    for emp in employees:
        if emp.get("id") == emp_id:
            return emp
    return "Employee not found"