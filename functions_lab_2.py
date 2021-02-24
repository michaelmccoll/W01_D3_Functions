tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 }
]

# Task 1: Print a list of uncompleted tasks
print(" ")
print("Task #1 _____")

def find_uncompleted_tasks(uncompleted_tasks):
    filtered_tasks = []
    for task in uncompleted_tasks:
        if task["completed"] == False:
            filtered_tasks.append(task)
    return filtered_tasks

uncompleted_task_list = find_uncompleted_tasks(tasks)
print(uncompleted_task_list)

# Task 2: Print a list of completed tasks
print(" ")
print("Task #2 _____")

def find_completed_tasks(completed_tasks):
    filtered_tasks = []
    for task in completed_tasks:
        if task["completed"] == True:
            filtered_tasks.append(task)
    return filtered_tasks

completed_task_list = find_completed_tasks(tasks)
print(completed_task_list)

# Task 3: Print a list of all task descriptions
print(" ")
print("Task #3 _____")

for task in tasks:
    print(task["description"])

# Task 4: Print a list of tasks where time_taken is at least a given time
print(" ")
print("Task #4 _____")

def task_time(times):
    result_times = []
    for task in times:
        if task["time_taken"] > 20:
            result_times.append(task)
    return result_times

tasks_over = task_time(tasks)
print(tasks_over)

# Task 5: Print any task with a given description
print(" ")
print("Task #5 _____")

def find_task_by_desc(task_list, task_desc):
    result_task = None
    for task in task_list:
        if task["description"] == task_desc:
            result_task = task
    return result_task

found_task = find_task_by_desc(tasks, "Feed Cat")
print(found_task)  

# # Task 6: Given a description update that task to mark it as complete.
# print("Task #6 _____")
# print(" ")

# # Task 7: Add a task to the list
# print("Task #7 _____")
# print(" ")

# # Task 8: Use a while loop to display the following menu and allow the use to enter an option.
# print("Task #8 _____")
# print(" ")

# # Task 9: Call the appropriate function depending on the users choice.
# print("Task #9 _____")
# print(" ")
