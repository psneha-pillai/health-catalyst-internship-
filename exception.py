def safe_productivity_score(task_completed, hours_worked):
    return task_completed / hours_worked

try:
    task_completed = int(input("Enter how many tasks are completed: "))

    if task_completed == 0:
        raise ValueError("Tasks completed cannot be zero")

    hours_worked = int(input("Enter worked hours by the employee: "))

    score = safe_productivity_score(task_completed, hours_worked)
    print("Productivity Score:", score)

except ValueError:
    print("please enter valid input")
except ZeroDivisionError:
    print("hours worked cannot be zero")
