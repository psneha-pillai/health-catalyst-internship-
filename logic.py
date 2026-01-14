'''Operations and Control Flow
File: logic.py
Ask the user to input hours worked.
Use if/elif/else to classify:
Underworked (<20 hours)
Normal (20–40 hours)
Overtime (>40 hours)
Use a for loop to print all employee names.
Use a while loop to repeatedly ask for a task until the user types ""done"".'''
hours=int(input("enter the worked hours"))
if hours<20:
    print("underworked")
elif 20 <= hours <= 40:
    print("Normal")
else:
    print("Overtime")
name=['sneha','sindhu','priya']
for i in name:
    print(i)
while True:
    task=input("enter task name,if u enter done the task will be stopped:")
    if task=='done':
        break
    print(task)