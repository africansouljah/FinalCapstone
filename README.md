# Concept of the task:

This project is a simple inventory management system for shoes. It allows the user to add new shoes to the inventory, view all the shoes in the inventory, search for a shoe by product code, re-stock shoes, and compute the total value of each shoe in the inventory.

The Shoe class has six attributes: country, code, product, cost, quantity, and sale_price. The class also has methods to get the cost and quantity attributes and a method to return a formatted string that includes all the attributes.

# Code Exaplation:

The given code defines a class named "Shoe" that has six attributes: country, code, product, cost, quantity, and sale_price. The class has several methods that allow adding new Shoe objects, displaying Shoe objects, restocking, searching for a specific Shoe object, and computing the value per item of each Shoe object.

The __init__ method initializes the class attributes with the provided values. The sale_price parameter is optional and has a default value of 0. Two other methods, get_cost() and get_quantity(), return the cost and quantity attributes, respectively. The __str__ method returns a formatted string that includes the product, country, code, quantity, cost, and sale_price attributes.

The code creates an empty list called shoe_list outside the class definition. The read_shoes_data function reads data from a file called "inventory.txt" and creates a Shoe object for each line of data in the file. The Shoe objects are appended to the shoe_list.

The capture_shoes() function prompts the user to enter information for a new Shoe object and creates one based on the input. The Shoe object is then appended to the shoe_list.

The view_all() function prints a table of all Shoe objects in the shoe_list. If the list is empty, it prints a message indicating that there are no shoes in the inventory.

The re_stock() function finds the Shoe object with the lowest quantity in the shoe_list, prompts the user to enter the number of items to add to the stock, and updates the quantity attribute of the Shoe object. The function also updates the corresponding line in the "inventory.txt" file with the new quantity value.

The search_shoe() function prompts the user to enter a product code and searches the shoe_list for a Shoe object with that code. If found, the function prints the Shoe object; otherwise, it prints a message indicating that no shoe was found.

The value_per_item() function computes the total value of each Shoe object in the shoe_list and displays the results in a table.


# To install project, follow these steps:

First, go to the project's GitHub page.
Click on the "Code" button and then click on "Download ZIP". This will download the project as a ZIP file.
Extract the ZIP file to a location on your computer where you want to store the project.
Open a terminal or command prompt window and navigate to the project's directory.
Install any required dependencies by running the appropriate command. This will depend on the project and the programming language used.
Run the project by executing the appropriate command or running the main file.

<img width="722" alt="Screenshot 2023-03-10 at 14 45 24" src="https://user-images.githubusercontent.com/119043038/224345889-950a033b-8907-4389-a5d3-dd9eadfadbdf.png">
<img width="607" alt="Screenshot 2023-03-10 at 14 45 44" src="https://user-images.githubusercontent.com/119043038/224345912-8d191c4a-962d-4444-a4bb-b12679fad3d5.png">

