# analytics.py

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

hours = float(input("Enter working hours: "))
rate = float(input("Enter hourly rate: "))
print("Total Pay:", calculate_pay(hours, rate))

n = int(input("\nEnter number of employees (hours list): "))
hours_list = []

for i in range(n):
    h = float(input(f"Enter hours for employee {i+1}: "))
    hours_list.append(h)

max_h, min_h, avg_h = employee_statistics(hours_list)
print("Maximum Hours:", max_h)
print("Minimum Hours:", min_h)
print("Average Hours:", avg_h)
employees = []
m = int(input("\nEnter number of employees (details): "))

for i in range(m):
    emp_id = int(input("Enter employee ID: "))
    name = input("Enter employee name: ")
    branch = input("Enter employee branch: ")
    employees.append({"id": emp_id, "name": name, "branch": branch})

search_id = int(input("\nEnter employee ID to search: "))
result = search_employee(employees, search_id)
print("Search Result:", result)
