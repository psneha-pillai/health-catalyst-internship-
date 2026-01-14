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
