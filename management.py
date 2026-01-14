'''2.1 List of Employees
Create a list of employee dictionaries.
Add a new employee to the list.
Remove an employee from the list.
Print the total number of employees.'''
employees = [
    {'id': 101, 'name': 'sneha', 'branch': 'cse'},
    {'id': 102, 'name': 'jitesh', 'branch': 'cse'}
]
new_employee = {'id': 103, 'name': 'rahul', 'branch': 'ece'}
employees.append(new_employee)
employees.remove({'id': 101, 'name': 'sneha', 'branch': 'cse'})
'''for emp in employees:
    if emp['name']=='sneha':
        employees.remove(emp)'''
print('Total no of employees:',len(employees))
print(employees)


'''2.2 Task Dictionary
Create a dictionary where keys are employee IDs and values are lists of assigned tasks.
Add a task to an employee.
Remove a task from an employee.
Print all tasks for all employees.'''
Dict={
    101:["online sessions"],
    102:["ETL","Mentoring"],
    103:["Managing","condacting classes"],
    104:["deployment","Migration"]
}
Dict[101].append('Migration')#adding a new task for the employee 101
Dict[104].append('ETL')#adding a new task for the employee 104

'''Dict[102].remove('ETL')#removing a task from 102 
Dict[102].remove("Mentoring")#removing a task from 102 completly becouse romove can remove one element at a time'''
for task in ["Managing", "condacting classes"]:#doing the same thing using loops
    if task in Dict[103]:
        Dict[103].remove(task)

print("Employee Tasks:")
for emp_id, tasks in Dict.items():
    print(f"Employee {emp_id}: {tasks}")

'''2.3 Unique Skills Using Sets
Create a set containing all unique employee skills.
Add two new skills to the set.
Print the final set of skills.'''
skills = {"Drawing", "Photography", "Singing"}
skills.add('python')
skills.add("wed_development")
print("end result of skills:",skills)


'''2.4 Company Holidays Using Tuples
Create a tuple of company holiday dates.
Attempt to change an element and if it fails, Write a comment explaining it.'''
holidays = ("2025-01-25", "2026-08-15", "2027-10-02")
holidays[0] = "2026-01-01"

# TypeError:'tuple' object  does not support item assignment error occurs because tuples are immutable.
# Once created, tuple values cannot be changed.
# added or removed. This makes tuples suitable for fixed data
