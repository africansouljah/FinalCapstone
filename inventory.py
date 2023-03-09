
class Shoe:
# This code defines a class called Shoe that has six attributes: country, code, product, cost, quantity, and sale_price.
# The __init__ method initializes these attributes with the provided values. The sale_price parameter is optional and defaults to 0.
    def __init__(self, country, code, product, cost, quantity, sale_price=0):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        self.sale_price = sale_price

 # The class also has two methods, get_cost() and get_quantity(), which return the cost and quantity attributes, respectively.
    def get_cost(self):
        return self.cost 
      
    def get_quantity(self):
        return self.quantity
# The __str__ method returns a formatted string that includes the product, country, code, quantity, cost, and sale_price attributes.
    def __str__(self):
        return f"{self.product} from {self.country} (Code: {self.code}) - {self.quantity} available at ${self.cost} each, Sale price is {self.sale_price}"

# The code then creates an empty list called shoe_list outside the class definition.
shoe_list = []

# The read_shoes_data function attempts to open a file called "inventory.txt" in read mode and reads the lines in the file. The first line is skipped because it contains the header.
# For each subsequent line, the function strips the newline character and splits the line on commas to obtain the data for a single Shoe object. The data is used to create a Shoe object, which is appended to the shoe_list.

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as f:
            next(f)  # skip header line
            for line in f:
                data = line.strip().split(",")
                shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                shoe_list.append(shoe)
    except FileNotFoundError:
        print("Error: inventory file not found")

# The capture_shoes() function prompts the user to enter information for a new Shoe object and creates one based on the input. The Shoe object is then appended to the shoe_list.
def capture_shoes():
    country = input("Enter the country of origin: ")
    code = input("Enter the product code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost per item: "))
    quantity = int(input("Enter the quantity available: "))
    shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(shoe)

# The view_all() function prints a table of all Shoe objects in the shoe_list. 
# If the list is empty, it prints a message indicating that there are no shoes in the inventory. 
# The function uses the headers list to define the column headers and rows list comprehension to create a list of rows to be displayed in the table. 
# The max_lengths list comprehension computes the maximum length for each column based on the data in the headers and rows lists. 
# The row_format string is constructed using the maximum lengths of each column, and the format() method is used to format the table
def view_all():
    if not shoe_list:
        print("No shoes in inventory")
        return
    headers = ["Product", "Cost", "Quantity", "Sale Price"]
    rows = [[s.product, s.cost, s.quantity, s.sale_price] for s in shoe_list]
    max_lengths = [max(max(map(len, str(x))), len(header)) for x, header in zip(rows, headers)]
    row_format = "".join(["{{:<{}}}".format(ml + 2) for ml in max_lengths])
    print(row_format.format(*headers))
    for row in rows:
        print(row_format.format(*row))

# The re_stock() function finds the Shoe object with the lowest quantity in the shoe_list, prompts the user to enter the number of items to add to the stock, and updates the quantity attribute of the Shoe object. 
# The function also updates the corresponding line in the "inventory.txt" file with the new quantity value.
def re_stock():
    if not shoe_list:
        print("No shoes in inventory")
        return
    shoe = min(shoe_list, key=lambda x: x.quantity)
    print(f"{shoe.product} (Code: {shoe.code}) has the lowest quantity available ({shoe.quantity})")
    add_qty = int(input("How many items do you want to add to the stock? "))
    shoe.quantity += add_qty
    with open("inventory.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        f.write(lines[0])
        for line in lines[1:]:
            data = line.strip().split(",")
            if data[1] == shoe.code:
                data[4] = str(shoe.quantity)
                line = ",".join(data) + "\n"
            f.write(line)
        f.truncate()

# The search_shoe() function prompts the user to enter a product code and searches the shoe_list for a Shoe object with that code. If found, the function prints the Shoe object; otherwise, it prints a message indicating that no shoe was found.
def search_shoe():
    code = input("Enter the product code: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe)
            return
    print(f"No shoe with code {code} found")
# The value_per_item() function computes the total value of each Shoe object in the shoe_list and displays the results in a table. 
# The headers list defines the column headers, and the data list comprehension creates a list of rows to be displayed in the table. 
# The max_lengths list comprehension computes the maximum length for each column based on the data in the headers and data lists. 
# The row_format string is constructed using the maximum lengths of each column, and the format() method is used to format the table.
def value_per_item():
    if not shoe_list:
        print("No shoes in inventory")
        return
    print("Value per item:")
    headers = ["Product", "Value"]
    data = [[s.product, s.cost * s.quantity] for s in shoe_list]
    max_lengths = [max(map(len, map(str, col))) for col in zip(headers, *data)]
    row_format = "".join(["{:<" + str(length) + "}" for length in max_lengths])
    print(row_format.format(*headers))
    for row in data:
        print(row_format.format(*row))
# The highest_qty() function finds the Shoe object with the highest quantity in the shoe_list and prints its details. 
# If the list is empty, the function prints a message indicating that there are no shoes in the inventory.
def highest_qty():
    if not shoe_list:
        print("No shoes in inventory")
        return
    shoe = max(shoe_list, key=lambda x: x.quantity)
    print(f"The {shoe.product} (Code: {shoe.code}) is for sale with the highest quantity ({shoe.quantity})")

# The read_shoes_data() function reads data from the "inventory.txt" file and creates a Shoe object for each line of data. 
# The Shoe objects are appended to the shoe_list. If the file is not found, the function prints an error message
read_shoes_data()

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:
    print("Shoe Inventory Management System")
    print("1. Read shoes data")
    print("2. Capture shoes")
    print("3. View all")
    print("4. Re-stock")
    print("5. Search shoe")
    print("6. Value per item")
    print("7. Highest quantity")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Try again.")        

