#=====importing libraries===========
from datetime import date  # Importing date in order to get the current date. 
today = date.today()

# Setting the variables needed 

user_data = {}
tasks_num = 0
users_num = 0

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
            admin_menu = input("Welcome to the admin menu please select one of the following: r - register a new user, a - add a task, va - view all tasks, vm - view my tasks, d - display statistics & e - exit: ").lower()
            print()
            if admin_menu == "r":
                username = input("Enter a new username: ") # Ask user to input a user name.
                password = input("Enter a new password: ") # Ask user to input a pass word.
                confirm_password = input("Confirm your password: ") # Asks usee to confirm their password.
                if password == confirm_password:
                    with open("user.txt", "a") as file:
                        file.write(username + "," + password +"\n")
                        print("User has been successfully registered!") # If the password match the programme will return the users username and password with a message to confirm that they've been registered
                    file.close 
                else:
                    print("Passwords do not match.")
            if admin_menu ==  "a":
                assigned_to = input("Enter the username of the person the task is assigned to: ")
                title = input("Enter the title of the task: ")
                description = input("Enter the description of the task: ")
                due_date = input("Enter the due date of the task (DD/MM/YYYY): ")
                current_date = today.strftime("%d/%m/%y")
                task = f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n" #This is the format we want to print the details in the tasks.txt file on a new line.
                with open ("tasks.txt", "a") as file: # using the a function to add to the file and storing tasks.txt as file.
                    file.write(task) # now we are telling the program to write the task in the file(tasks.txt)
                file.close
                print("Task has been added to tasks.txt!")
            if admin_menu == "va":
                with open("tasks.txt", "r") as file:
                    for line in file:
                        task_data = line.strip().split(", ")
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
            if admin_menu == "vm":
                with open("tasks.txt", "r") as f:
                    for line in f:
                        task = line.strip().split(", ") # Stripping the spaces in the lines and splitting the variables with a comma. 
                        if task[0] == username: # checks that first value of the task 'list' matches the user logged in then prints any tasks relevant to the user logged in.
                            print(f"Assigned to: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nDue date: {task[3]}\nDate added: {task[4]}\nCompleted: {task[5]}\n")
                    f.close
# This code is using the with open statement to open two files, "tasks.txt" and "user.txt".
# The for line in task_file loop reads each line of the task_file and increments.
# The tasks_num variable by 1 for each line. After reading all lines, the code prints the total number of tasks in the file by using the f-string to insert the value of the tasks_num variable into the string.
            if admin_menu == "d":
                with open("tasks.txt", "r") as task_file:
                    for line in task_file:
                        tasks_num += 1
                    print (f"\nTotal number of tasks: {tasks_num}\n")
                    task_file.close
                with open("user.txt", "r") as username:
                    for line in username:
                        users_num += 1
                    print (f"Total number of users: {users_num}\n")
                    username.close
            if admin_menu == "e":
                print('Goodbye', username)
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
        if username == 'admin':

            username = input("Enter a new username: ") # Ask user to input a user name.
            password = input("Enter a new password: ") # Ask user to input a pass word.
            confirm_password = input("Confirm your password: ") # Asks usee to confirm their password.
            if password == confirm_password:
                with open("user.txt", "a") as file:
                    file.write(username + "," + password +"\n")
                    print("User has been successfully registered!") # If the password match the programme will return the users username and password with a message to confirm that they've been registered
                file.close 
            else:
                print("Passwords do not match.") # If passwords don't match user will receive a message saying the passwords dont match.
        else:
            print("You're not admin. You cannot choose this option")
        

# **** ASSIGNING A TASK TO USER ****
 # This code prompts the user for the username of the person the task is assigned to, the title of the task, a description of the task, and the due date of the task.
# Then it gets the current date using the datetime library, and creates a string with all the information.

    elif menu == 'a': # Once a is selected from the menu. programme prompts the user to enter details of the task and user.
        assigned_to = input("Enter the username of the person the task is assigned to: ")
        title = input("Enter the title of the task: ")
        description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task (DD/MM/YYYY): ")
        current_date = today.strftime("%d/%m/%y")
        task = f"{assigned_to}, {title}, {description}, {due_date}, {current_date}, No\n" #This is the format we want to print the details in the tasks.txt file on a new line.
        with open ("tasks.txt", "a") as file: # using the a function to add to the file and storing tasks.txt as file.
            file.write(task) # now we are telling the program to write the task in the file(tasks.txt)
        file.close
        print("Task has been added to tasks.txt!")

# **** READING A TASK ****
# This code reads the file line by line and for each line, it strips the leading/trailing whitespaces and splits the line by comma and space.
# Then it assigns each element of the resulting list to a variable and prints the variables in the desired format.
    elif menu == 'va':
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(", ")
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

# **** READING USER LOGGED IN TASK ****
    elif menu == 'vm':
        with open("tasks.txt", "r") as f:
            for line in f:
                task = line.strip().split(", ") # Stripping the spaces in the lines and splitting the variables with a comma. 
                if task[0] == username: # checks that first value of the task 'list' matches the user logged in then prints any tasks relevant to the user logged in.
                    print(f"Assigned to: {task[0]}\nTitle: {task[1]}\nDescription: {task[2]}\nDue date: {task[3]}\nDate added: {task[4]}\nCompleted: {task[5]}\n")
            f.close

        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")