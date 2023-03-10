# Concept of the task:

In this task, I will be creating a program for a small business that will help them to manage tasks assigned to each member of their team.

# Code explaination:

This is a Python script that allows users to register new accounts, add tasks and view all tasks. It also allows administrators to view statistics on the number of tasks and registered users.

The script starts by importing the date module from the datetime library to get the current date. It then sets up a dictionary to store user data and variables for the number of tasks and registered users.

The script then reads user data from a text file and stores it in the user_data dictionary. It then enters a login loop where it prompts the user to enter their username and password. If the username and password are correct, the user is granted access and the loop breaks. Otherwise, the user is prompted to enter their details again.

If the user is an admin, they are presented with an admin menu where they can register a new user, add a task, view all tasks, view their tasks, view statistics or exit.

If the user is not an admin, they are presented with a regular menu where they can register a new user or add a task.

When the user selects the "register user" option, they are prompted to enter a new username and password. If the passwords match, the new user is added to the user_data dictionary and the details are written to the user.txt file.

When the user selects the "add task" option, they are prompted to enter the username of the person the task is assigned to, the title of the task, the description of the task, and the due date of the task. The current date is also recorded and added to the tasks.txt file.

When the user selects the "view all tasks" option, the script reads the tasks.txt file and prints out all tasks.

When the user selects the "view my tasks" option, the script reads the tasks.txt file and prints out only the tasks assigned to the current user.

When the admin selects the "display statistics" option, the script reads the tasks.txt and user.txt files and counts the number of tasks and registered users. These counts are then printed to the console.

Finally, when the user selects the "exit" option, the program ends.


# To install project, follow these steps:

First, go to the project's GitHub page.
Click on the "Code" button and then click on "Download ZIP". This will download the project as a ZIP file.
Extract the ZIP file to a location on your computer where you want to store the project.
Open a terminal or command prompt window and navigate to the project's directory.
Install any required dependencies by running the appropriate command. This will depend on the project and the programming language used.
Run the project by executing the appropriate command or running the main file.

<img width="1432" alt="Screenshot 2023-03-09 at 23 30 58" src="https://user-images.githubusercontent.com/119043038/224184243-a7c82169-a765-475b-8329-3983bf6613a1.png">
<img width="1439" alt="Screenshot 2023-03-09 at 23 31 31" src="https://user-images.githubusercontent.com/119043038/224184272-bdc83fea-7d0d-470b-add6-48f331461e9f.png">
