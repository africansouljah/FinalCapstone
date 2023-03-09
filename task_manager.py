#=====importing libraries===========
import datetime
from datetime import date  # Importing date in order to get the current date. 
today = date.today()

# Setting the variables needed 

user_data = {}
tasks_num = 0
users_num = 0

# Setting the variables need for our functions
username = []
password = []
confirm_password = []

# ====== FUNCTIONS ======
# Registering a new user.
# In this function, the existing usernames are read from the file and stored in the users list. Then, the new username is checked against the list of existing usernames.
# If it already exists, an error message is displayed. Otherwise, the new username is added to the file.
def reg_user():
    username = input("Enter a new username: ")
    with open("user.txt", "r") as file: # Open the "user.txt" file in read mode and read its contents
        users = file.readlines() # Read the contents of the file into a list of strings
        users = [user.strip().split(",")[0] for user in users] # Create a new list of only usernames (the first element of each split line)
    if username in users: # Check if the input username already exists in the list of usernames
        print("Error: username already exists. Please choose another one!")  # If the username already exists, print an error message
        return
    password = input("Enter a new password: ") # Input for new password
    confirm_password = input("Confirm the password: ") # Input to confirm password
    if password == confirm_password: # Check if the password and confirmation match
        with open("user.txt", "a") as file:  # If the passwords match, write the new username and password to the "user.txt".
            file.write(username + "," + password +"\n")
            print(username,"has been successfully registered!\n")  # Print a success message
    else:
        print("Passwords do not match.")  # If the passwords don't match, print an error message
        file.close
    file.close

# Adding a task to user
# This code is a Python script that creates a function named "adduser". This function takes input from the user in the form of strings.
 # This code prompts the user for the username of the person the task is assigned to, the title of the task, a description of the task, and the due date of the task.
# Then it gets the current date using the datetime library, and creates a string with all the information.
def assign_task():
    assigned_to = input("Enter the username of the person the task is assigned to: ")
    title = input("Enter the title of the task: ")
    description = input("Enter the description of the task: ")
    due_date = input("Enter the due date of the task (DD/MM/YYYY): ")
    current_date = today.strftime("%d/%m/%y")
    task = f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n" #This is the format we want to print the details in the tasks.txt file on a new line.
    with open ("tasks.txt", "a") as file: # using the a function to add to the file and storing tasks.txt as file.
            file.write(task) # now we are telling the program to write the task in the file(tasks.txt)
    print("Task has been added to tasks.txt!")

# Viewing all tasks
# This code reads the file line by line and for each line, it strips the leading/trailing whitespaces and splits the line by comma and space.
# Then it assigns each element of the resulting list to a variable and prints the variables in the desired format.
# This code defines a Python function named "view_tasks". The function opens a text file named "tasks.txt" in read mode ('r') using the with statement and the file object is stored as "file".
# The function then loops over the lines in the file using a for loop. For each line, it removes the white space using the strip() method and splits the line into a list of values using the split(', ') method.
# The values are then assigned to different variables such as task_number, task_name, task_description, and task_deadline.
# Finally, the function prints the task details.
def view_tasks():
    with open("tasks.txt", "r") as file:
        for line in file:
            task_data = line.strip().split(",")# Stripping the spaces in the lines and splitting the variables with a comma and storing the strings in the variable called task_data.
            task_number = task_data[0]
            task_name = task_data[1]
            task_description = task_data[2]
            task_deadline = task_data[3]
            print("Task Number:", task_number)
            print("Task Name:", task_name)
            print("Task Description:", task_description)
            print("Task Deadline:", task_deadline)
            print()
    file.close

# View my tasks
# This code defines a Python function named "view_my_tasks". The function opens a text file named "tasks.txt" in read mode ('r') using the with statement and the file object is stored as "f".
# The function then loops over the lines in the file using a for loop. For each line, it removes the white space using the strip() method and splits the line into a list of values using the split(', ') method. The list is stored as the "task" variable.
# The function then uses an if statement to check if the first value of the "task" list (i.e. the assigned user) matches a username stored in the variable named "username".
# If the condition is true, the function prints the task details, including the assigned user, title, description, due date, date added, and completion status, using formatted string literals (f-strings).
def view_my_tasks():
    tasks = [] # Initialize an empty list to store tasks
    with open("tasks.txt", "r") as f: # Open the file 'tasks.txt' in read mode and store it in the variable 'f'
        lines = f.readlines() # Read all the lines in the file 'tasks.txt' and store it in the variable 'lines'
        for i, line in enumerate(lines): # Loop through the 'lines' list with the index 'i'
            task = line.strip().split(",") # Stripping the spaces in the lines and splitting the variables with a comma. 
            if task[0] == username: # checks that first value of the task 'list' matches the user logged in then prints any tasks relevant to the user logged in.
                print(f"Task number: {i+1}\nAssigned to: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nDue date: {task[3]}\nDate added: {task[4]}\nCompleted?: {task[5]}\n")
                tasks.append(task)# Append the 'task' to the 'tasks' list
    task_choice = int(input("Enter the task number you want to view in detail (-1 to return to main menu): "))
    if task_choice == -1:
        return
    if task_choice > 0 and task_choice <= len(tasks): #Checking is the users input matches the range of the list if nor prints an error message. If yes proceed. 
        task = tasks[task_choice-1]
    else:
        print("Task number not found.")
        return
    task = tasks[task_choice-1] # Retrieve the task the user wants to view in detail by its task number
    if task[5] == "Yes":  # Check if the task has already been completed
        print("Task has already been completed and cannot be edited.")
        return
    action = input("Do you want to mark the task as complete (c) or edit the task (e)? ")
    if action == "c":
        lines[task_choice-1] = ",".join(task[:5] + ["Yes"] + ["\n"]) # Join the task list with a comma and add 'Yes' as the completion status, then replace the original line in 'lines' with this new line
        with open("tasks.txt", "w") as f:
            f.writelines(lines) # Write the updated 'lines' back to the file
    elif action == "e":
        field = input("Do you want to edit the username (u) or the due date (d)? ")
        if field == "u":
            task[0] = input("Enter the new username: ") # Replace the first element in 'task' (the username) with the new username
        elif field == "d":
            task[3] = input("Enter the new due date: ") # Replace the fourth element in 'task' (the due date) with the new due date
        lines[task_choice-1] = ",".join(task) + "\n" # Join the task list with a comma, add a newline character, and replace the original line in 'lines' with this new line
        with open("tasks.txt", "w") as f:
            f.writelines(lines)
    else:
        print("Invalid input. No changes made.")
    f.close

# Display statistics
# This code is using the with open statement to open two files, "tasks.txt" and "user.txt".
# The for line in task_file loop reads each line of the task_file and increments.
# The tasks_num variable by 1 for each line. After reading all lines, the code prints the total number of tasks in the file by using the f-string to insert the value of the tasks_num variable into the string.

def display_statistics():
    try:  # Try to open task_overview.txt and read its contents
        with open("task_overview.txt", "r") as task_file:
            tasks = task_file.read()
            print(f"Task Overview:\n{tasks}")
         # If task_overview.txt doesn't exist, generate it and read its contents
    except FileNotFoundError:
        generate_task_overview()
        with open("task_overview.txt", "r") as task_file:
            tasks = task_file.read()
            print(f"Task Overview:\n{tasks}")
    try: # Try to open user_overview.txt and read its contents
        with open("user_overview.txt", "r") as user_file:
            users = user_file.read()
            print(f"\nUser Overview:\n{users}")
        # If user_overview.txt doesn't exist, generate it and read its contents
    except FileNotFoundError:
        generate_user_overview()
        with open("user_overview.txt", "r") as user_file:
            users = user_file.read()
            print(f"\nUser Overview:\n{users}")

# Generating the task over views.
def generate_task_overview():
    tasks = []
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

    with open("tasks.txt", "r") as file: # Open the file tasks.txt in read mode.
        tasks = file.readlines()
        
    total_tasks = len(tasks) # Get the total number of tasks
    
    for task in tasks: # Loop through all the tasks in the tile.
        task_details = task.strip().split(",")
        if len(task_details) >= 6: #If the task has at least 6 values, process it 
            due_date = datetime.datetime.strptime(task_details[3].strip(),"%d/%m/%Y") # Convert the due date string to a datetime object.
            if task_details[-1] == "Yes": #Check if the task completed. 
                completed_tasks += 1
                completed_date = datetime.datetime.strptime(task_details[-2].strip(),"%d/%m/%Y") # Convert the completion date string to a datetime object.
                if completed_date > due_date: #Check if the completion date is after the due date.
                    print("Warning: Task", task_details[0], "was completed after its due date.")
            else:
                uncompleted_tasks += 1
                # Check is the due date has passed.
                if due_date < datetime.datetime.today():
                    overdue_tasks += 1
        # If the tasks doesn't have the correct format skip it. 
        else:
            print("Skipping task with incorrect format: ", task) 
# Calculate the percentage of incomplete tasks.
    incomplete_percentage = (uncompleted_tasks / total_tasks) * 100
# Calculate the percentage of overdue tasks. 
    overdue_percentage = (overdue_tasks / total_tasks) * 100

#Open the task_overview.txt in write mode. 
    with open("task_overview.txt", "w") as file:
        file.write("Total tasks: " + str(total_tasks) + "\n")
        file.write("Completed tasks: " + str(completed_tasks) + "\n")
        file.write("Uncompleted tasks: " + str(uncompleted_tasks) + "\n")
        file.write("Overdue tasks: " + str(overdue_tasks) + "\n")
        file.write("Percentage of incomplete tasks: " + str(incomplete_percentage) + "%\n")
        file.write("Percentage of overdue tasks: " + str(overdue_percentage) + "%\n")
        
    print("Task overview generated successfully!")


# Generating the user overview. 
def generate_user_overview():
    with open("tasks.txt", "r") as file:  # Open the tasks.txt file in read mode and read its contents into the `tasks` variable
        tasks = file.readlines()

    total_tasks = len(tasks) # Calculate the total number of tasks

    users = {} # Initialize a dictionary to store the task overview for each user
    for task in tasks:  # Iterate over the tasks
        task = task.strip().split(", ")  # Split the task into its component parts
        username = task[0]
        description = task[1]
        due_date = task[3]
        status = task[:6]

        if username not in users: # If the username is not already in the `users` dictionary, add it with the default values
            users[username] = {"total_tasks": 0, "completed": 0, "overdue": 0}

        users[username]["total_tasks"] += 1 # Increment the number of total tasks for the user

        if status == "Yes":  # If the task is completed, increment the number of completed tasks for the user
            users[username]["completed"] += 1
        elif due_date < today.strftime("%d/%m/%y"):  # If the task is overdue, increment the number of overdue tasks for the user
            users[username]["overdue"] += 1

    with open("user_overview.txt", "w") as file: # Open the user_overview.txt file in write mode
         # Write the total number of users and the total number of tasks to the file
        file.write(f"Total number of users: {len(users)}\n")
        file.write(f"Total number of tasks: {total_tasks}\n\n")

        for user in users:  # Iterate over the users
             # Get the number of tasks assigned to the user, the number of completed tasks, and the number of overdue tasks
            user_tasks = users[user]["total_tasks"]
            user_completed = users[user]["completed"]
            user_overdue = users[user]["overdue"]
            user_pending = user_tasks - user_completed - user_overdue  # Calculate the number of pending tasks
# Write the user's task overview to the file.
            file.write(f"Username: {user}\n")
            file.write(f"Total tasks assigned: {user_tasks}\n")
            file.write(f"Percentage of total tasks: {(user_tasks / total_tasks) * 100:.2f}%\n")
            file.write(f"Percentage of tasks completed: {(user_completed / user_tasks) * 100:.2f}%\n")
            file.write(f"Percentage of tasks pending: {(user_pending / user_tasks) * 100:.2f}%\n")
            file.write(f"Percentage of tasks overdue: {(user_overdue / user_tasks) * 100:.2f}%\n\n")
        
        print("User overview has been generated!")


#====Login Section====
# Read user data from user.txt file and store in a dictionary.
with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(",")
        user_data[username] = password
# Login loop
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_data and user_data[username] == password:
        print("Welcome, " + username + "!")
        break
    else:
        print("Invalid username or password. Please try again.")

# ***** ADMIN MENU ****** 
# This code below is the same as the previous code however,  its specified for for only admin inputs.
# i have added the d input so the admin can view the statistics in the number of users and tasks.
while True:   
        if username == "admin":
            admin_menu = input("""Welcome to the admin menu please select one of the following:
r - register a new user
a - add a task
va - view all tasks 
vm - view my tasks
gr - generate report
d - display statistics 
e - exit: """).lower()
            print()
            if admin_menu == "r":
                reg_user()
                print("")
            if admin_menu ==  "a":
                assign_task()
                print("")
            if admin_menu == "va":
                view_tasks()
                print("")
            if admin_menu == "vm":
                view_my_tasks()
                print("")
            if admin_menu == "d":
                display_statistics()
                print("")
            if admin_menu == "gr":
                generate_task_overview()
                print("")
                generate_user_overview()
                print("")     
            if admin_menu == "e":
                print('Goodbye', username + "!")
                exit()
        else:
            break

while True:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()
# **** REGISTERING A USER ****
    if menu == 'r':
        print("You're not admin. You cannot choose this option")
        
# **** ASSIGNING A TASK TO USER ****
    elif menu == 'a': # Once a is selected from the menu. programme prompts the user to enter details of the task and user.
        assign_task()

# **** READING A TASK ****
    elif menu == 'va':
        view_tasks()

# **** READING USER LOGGED IN TASK ****
    elif menu == 'vm':
        view_my_tasks()

    elif menu == 'e':
        print('Goodbye',username + "!")
        exit()

    else:
        print("You have made a wrong choice, Please Try again")