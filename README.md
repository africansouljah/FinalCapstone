# Concept of the task:

A continuation of the previous task. In this task, I will be creating a program for a small business that will help them to manage tasks assigned to each member of their team.

# Code Exaplation:

The code is a task management system that allows users to register, assign tasks to users, view tasks, and view tasks assigned to themselves.

The program starts by importing the required datetime and date libraries. It then defines some variables to store user data, the number of tasks, and the number of users. It also initializes empty lists to store user credentials such as usernames, passwords, and confirmed passwords.

The program defines four functions: reg_user, assign_task, view_tasks, and view_my_tasks.

The reg_user function prompts the user to input a new username and checks if it already exists in the user.txt file. If the username is not already in the file, the user is prompted to input a password, and the program writes the username and password to the user.txt file.

The assign_task function prompts the user to input the username of the person to whom the task is assigned, the title of the task, the task description, and the task's due date. The program then writes the details of the task to the tasks.txt file in a specific format.

The view_tasks function reads the contents of the tasks.txt file and prints out each task's details, including the task number, task name, task description, and task deadline.

The view_my_tasks function reads the contents of the tasks.txt file and displays the tasks assigned to the user who is currently logged in. The function then prompts the user to select a task to view in more detail. If the task has not been completed, the user can choose to mark the task as complete or edit the task.

<img width="1188" alt="Screenshot 2023-03-10 at 00 09 52" src="https://user-images.githubusercontent.com/119043038/224189797-e15eb40a-c1d6-44e8-908f-c8a0405441c3.png">
<img width="886" alt="Screenshot 2023-03-10 at 00 10 22" src="https://user-images.githubusercontent.com/119043038/224189809-e3b5fc19-ec85-4819-9cf8-703847aa78e1.png">
<img width="718" alt="Screenshot 2023-03-10 at 00 10 51" src="https://user-images.githubusercontent.com/119043038/224189812-5798f710-91e4-437c-9907-6e69aa28608b.png">
