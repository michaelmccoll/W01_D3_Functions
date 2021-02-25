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

def display_descriptions():
    for task in tasks:
        print(task["description"])

display_descriptions()

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

# Task 6: Given a description update that task to mark it as complete.
print(" ")
print("Task #6 _____")

def TBC():
    pass

# Task 7: Add a task to the list
print(" ")
print("Task #7 _____")

def add_task(desc,status,time):
    tasks.append({
        "description": desc,
        "completed": status,
        "time_taken": time})

add_task("Shower",True,"15")
print(tasks)

# Task 8: Use a while loop to display the following menu and allow the use to enter an option.
print(" ")
print("Task #8 _____")

menu = [
    "Menu:",
    "1: Display All Tasks",
    "2: Display Uncompleted Tasks",
    "3: Display Completed Tasks",
    "4: Mark Task as Complete",
    "5: Get Tasks Which Take Longer Than a Given Time",
    "6: Find Task by Description",
    "7: Add a new Task to list",
    "M or m: Display this menu",
    "Q or q: Quit"
]

def menu_display():
    for options in menu:
        print(options)

menu_display()

user_selection = int(input("Please select an option from the menu: "))
print(user_selection)

# Task 9: Call the appropriate function depending on the users choice.
print(" ")
print("Task #9 _____")

def quit():
    if user_selection == Q or user_selection == q:
        print("Quit")

def menu_func():
    if user_selection == M or user_selection == m:
        menu_display()

menu_functions = [
    {1: "Display All Tasks","function": display_descriptions()},
    {2: "Display Uncompleted Tasks","function": find_uncompleted_tasks()},
    {3: "Display Completed Tasks","function": find_completed_tasks()},
    {4: "Mark Task as Complete","function":TBC()},
    {5: "Get Tasks Which Take Longer Than a Given Time","function": task_time()},
    {6: "Find Task by Description","function": find_task_by_desc()},
    {7: "Add a new Task to list","function": add_task()},
    {M or m: "Display this menu","function": menu_func()},
    {Q or q: "Quit", "function": quit()}
]
