"""
SE T32 - Capstone Project IV - OOP

    ● Code a Python program that will read from the text file inventory.txt and
    perform the following on the data, to prepare for presentation to your
    managers:
        o We’ve provided a template for you in a file named inventory.py.
        o Inside this file, you will find a class named Shoe with the following
        attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
            ● etc ...   
"""

# =========== Importing libraries ============== #
from tabulate import tabulate
from color_pattern import *
import time

# ======== The beginning of the class ========== #
# Define parent class as shoe
class Shoe:
    """
    store objects in stock,contains the function
    and methods of the constructor.
    """
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # # Method to obtain the cost of products.
    def get_cost(self):
        return self.cost

    # Method to get quantity of the products.
    def get_quantity(self):
        return self.quantity

    # Method to return a string representation of the class.
    def __str__(self):
        return f"\n{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    # Method to make the class iterable.
    def __iter__(self):
        return iter([self.country, self.code, self.product, self.cost, self.quantity])


# ================ Shoe list =================== #

#List will be used to store a list of objects of products.
shoe_list = []

# ========= Functions outside the class ======== #
# Define function to Read shoe data from inventory.txt
def read_shoes_data():
    """
    Will open the Inventory.txt file, read the data from this file and create
    an object for the products with the internal data and add this object to
    the list of shoes.
    Try-except is used to handle situation when the file is not available.
    """
    try:
        with open("inventory.txt", "r", encoding='utf-8') as inventory:
            inventory_data = inventory.readlines()

        for shoe in inventory_data[1:]:
            shoe = shoe.strip().split(",")
            shoe_list.append(Shoe(shoe[0], shoe[1], shoe[2], float(shoe[3]), int(shoe[4])))

    except FileNotFoundError:
        show_red_black("File 'inventory.txt' does not exist.")

def capture_shoes():
    """
    User will capture data about a product and use that data to create
    a shoe object and place the object inside the shoes list.
    It also adds a new object to the Inventory.txt file.
    """
    country = input("Enter country name:\n").capitalize()
    show_line_green()

    code = input(f"Enter the product code:"
                 f"{YELLOW}\nExample SKU12345{END}\n").upper()
    show_line_green()

    product = input("Enter the product model:\n").title()
    show_line_green()

    while True:
        try:
            cost = float(input("Enter the value of the product:\n"))
            break
        except ValueError:
            show_red_black("Invalid input. Only numbers!")
    show_line_green()

    while True:
        try:
            quantity = int(input("Enter quantity to put in stock:\n"))
            break
        except ValueError:
            show_red_black("Invalid input. Only numbers!")

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new_shoe)

    try:
        with open("inventory.txt", "a") as inventory:
            inventory.write(str(new_shoe))
    except FileNotFoundError:
        show_red_black("File 'inventory.txt' does not exist.")

    show_back_green("New products successfully added to stock.")


def view_all():
    """
    Will print the details of products stored in the shoe list
    organized in a tabular format using the tabulate module.
    """
    if len(shoe_list) == 0:
        show_red_black("Inventory.txt is empty!")

    else:
        show_red_txt("All products currently available in the warehouse.")
        print(tabulate([shoe.__iter__() for shoe in shoe_list],
                       headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="psql"))

#  Define function to find shoe of lowest quantity to re-stock.
def re_stock():
    """
    It will find the shoe objects with the least amount,
    which are the products that need to be restocked.
    When the user adds the quantity of products, the list is updated.
    This amount must be updated in the file for this shoe.
    """
    if len(shoe_list) == 0:
        show_red_black("Inventory.txt is empty!")
        return

    min_quantity = min(shoe.quantity for shoe in shoe_list)
    shoes_to_restock = []
    for shoe in shoe_list:
        if shoe.quantity == min_quantity:
            shoes_to_restock.append(shoe)

    for shoe in shoes_to_restock:

        show_line_green()
        print(f"Product low stock! Model: {LIGHTRED}{shoe.product}{END} with the code: {LIGHTRED}{shoe.code}{END}."
              f"\nOnly available in stock {LIGHTRED}{shoe.quantity}{END} products.")

        while True:
            try:
                show_cyan("Enter the quantity if you want to restock or \"0\" "
                          "\nto return to the main menu.")
                add_quantity = int((input(":")))
                break
            except ValueError:
                show_red_black("Invalid input, integers only . Try again!")

        if add_quantity > 0:
            print("Updating stock system.....")
            time.sleep(3)
            show_line_green()

            shoe.quantity += add_quantity
            print(f"The Model: {GREEN}{shoe.product}{END}, Code: {GREEN}{shoe.code}{END}, stock has been updated."
                  f"\nCurrent quantity {GREEN}{shoe.quantity}{END} products.")

        elif add_quantity <= 0:
            break

    try:
        with open("inventory.txt", "w", encoding='utf-8') as inventory:
            inventory.write("Country,Code,Product,Cost,Quantity")
            for shoe in shoe_list:
                inventory.write(str(shoe))
    except FileNotFoundError:
        show_red_black("File 'inventory.txt' does not exist.")

# Define function to use shoe code to find shoe from list and print 
# the shoe selected.
def search_shoe(search_code):
    """
    This function will search for a product from the list
    using the product code and will return this object to be printed.
    """
    for shoe in shoe_list:
        if search_code == shoe.code:
            return shoe
        else:
            continue
    return None

# Define function that will calculate the total value for each item.
def value_per_item():
    """
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """

    show_red_2("------ Value of products in stock ------",
               "Value of each item x Quantity of each item in stock = R" )
    grand_total = 0
    values_list = []

    for shoe in shoe_list:

        value = (shoe.cost * shoe.quantity)
        values_list.append([shoe.product, shoe.code, shoe.cost, shoe.quantity, value])
        grand_total += value

    print (tabulate(values_list, headers=["Product", "Model", "Cost R", "Quantity", "Total Cost R"],
                       tablefmt= "psql"))


# You will receive the product with the largest quantity and print 
# the product for sale on sale.
def highest_qty():
    """
    Code will determine the product with the largest quantity and will
    print this product as being for sale.
    """
    max_qty = max(shoe.quantity for shoe in shoe_list)
    highest_qty_shoes = []
    for shoe in shoe_list:
        if shoe.quantity == max_qty:
            highest_qty_shoes.append(shoe)

    for shoe in highest_qty_shoes:
        print(f"{MAGENTA}{shoe.quantity}{END} items of the {MAGENTA}{shoe.product}{END} model,"
              f" are available on stock in the \ncountry {MAGENTA}{shoe.country}{END}.")

# ================= Main Menu ====================== #
# Display menu options using while.
# Create header variable so when we write over inventory, 
# headers are still there.
read_shoes_data()

while True:

    show_white(f"Shoe Inventory Management", "------ Main Menu ------")
    print(f"{YELLOW}"
          f"1 - List all products.\n"
          f"2 - Stock products with low stock - Update.\n"
          f"3 - Enter new products to stock.\n"
          f"4 - Search product by code.\n"
          f"5 - Display the value for each stocked product.\n"
          f"6 - Consult stock products released for sales promotion.\n"
          f"7 - Quit APP and save changes.{END}")

    show_cyan("What menu action do you want to take?")

    menu = input(":")

    if menu == "1":
        view_all()

    elif menu == "2":
        re_stock()

    elif menu == "3":
        capture_shoes()

    elif menu == "4":
        search_code = input("Enter the code of the shoes you would like to find:"
                            f"{YELLOW}\nExample SKU12345{END}\n").upper()
        shoe = search_shoe(search_code)

        if shoe:
            show_back_green("Product found in stock!")
            print(tabulate([shoe.__iter__()], headers=["Country ", "Code ", "Product ",
                                                       "Cost ", "Quantity "], tablefmt = "psql"))
        else:
            show_red_black(f"Product with code {search_code} not found in stock!")

    elif menu == "5":
        value_per_item()

    elif menu == "6":
        highest_qty()

    elif menu == "7":
        print("Preparing to exit the APP...")
        time.sleep(2)

        show_red_txt("You have exited the App. See you later!")
        break
    else:
        show_red_black_2("Invalid input.", "Enter an option from the menu.")



'''
References Used:

Most code was obtained help in some conversations and doubts via APP DISCORD
from the HyperionDev Software Engineering student group.
#---------------------------------------------------------------------------------#
SE T32 - Capstone Project IV - OOP.pdf
SE T32 - Capstone Project IV - OOP video
https://youtu.be/iB4mqqVZOq0
Author : HyperionDev 2023.
#---------------------------------------------------------------------------------#
Reference: Site GeeksForGeeks Python/
https://www.geeksforgeeks.org/
#---------------------------------------------------------------------------------#
Reference: Site W3 Schools Python/
https://www.geeksforgeeks.org/python-oops-concepts/
#---------------------------------------------------------------------------------#
# https://www.youtube.com/watch?v=vplseTRdbLM
#  https://www.youtube.com/watch?v=Yq0lbu8goeA
# https://www.youtube.com/watch?v=Smf68icE_as
#---------------------------------------------------------------------------------#
'''

