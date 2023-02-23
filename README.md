
## Footwear Manager - Capstone IV.

---
### Requirements.

- [X] Python 3.11 - [read more](https://www.python.org/downloads/release/python-3110/)
---
### What is the goal of this project?
- [X] This project was done using Python Programming and stored in an external .txt file. 
- [X] Provides the user with a complete tool to administer and manage products<br /> 
  within several footwear warehouses.

### Users are able to:
- [X] View existing stock => Displays a list of all products currently available in a user-friendly format.
- [X] Stock products with low stock => User can update the quantity in stock for a particular item.
- [X] Enter new products to stock => User can add a new product to the inventory containing all details.
- [X] Search for a specific product => Find product by code and show all storage information.
- [X] Calculates the value of product in stock => Shows the added value of each stocked product.
- [X] Consult stock products released for sales promotion => Products with large quantity stocked.
---
### Contents.

| Index                 | Description                                                 |
|-----------------------|-------------------------------------------------------------|
| Running the program.  | Important information before running the program.           |
| Creating an Shortcut. | Shows how to create a shortcut to run inventory.py desktop. |
| Stored external.      | Shows the database recorded in .txt.                        |
| Menu (1 to 7).        | Displays all options available to the user.                 |
| Credits.              | Method and materials used.                                  |


---
### 1) Running the Program.
- [X] To operate the programme, simply run inventory.py from a local directory.
- [X] IMPORTANT: Make sure inventory.txt is in the same directory as inventory.py.
- [X] Inventory.txt is the external file that stores all the warehouse information.

---
### 2) Creating an inventory.py shortcut to run without python open.
1) Open Notepad (or any text editor).
2) Write the following code:

![chortcut](https://user-images.githubusercontent.com/81885034/220776835-1646d02e-338e-45c7-be9a-5fbd554d96c1.png)

*Replace "path\to\your\python\script.py" with the path to your Python script.*

3) Save the file with a .bat extension (e.g. my_python_script.bat).
Make sure to choose<br /> "All Files" as the file type when saving.
4) Right-click on the .bat file and choose "Create shortcut".
5) Move the shortcut to your desktop or any location where you want the icon to appear.
6) Right-click on the shortcut and choose "Properties".
7) Click on the "Change Icon" button and select an icon of your choice.
8) Click "OK" to close the "Change Icon" dialog box, then click "Apply" and close the Properties dialog box.

*Now, when you double-click on the icon inventory.ba, it will run your Python script without opening Python.<br /> 
The command prompt window will briefly appear and then close once the script has finished running.*

 <img src="https://user-images.githubusercontent.com/81885034/220908107-6e01c215-dc27-402f-a6fb-42eea5415002.png" height="300"/>

---
### 3) Stored external Inventory.txt.

Each line of the file is a comma separated string in the following format:

Country, Code, Product, Cost, Quantity

<img src="https://user-images.githubusercontent.com/81885034/220915372-4a486030-1268-40df-bd8c-067f33916658.png" height="400"/>


*inventory.py can access these entries, edit them and create new entries in order to perform its functions.*

---
### 4) Menu.
The main menu presents the following options:

<img src="https://user-images.githubusercontent.com/81885034/220929022-ecace3d3-da69-41bf-9ff6-4181a6c255fd.png" height="300"/>

Choose the relevant ID number, then press ENTER to access the desired function.


- [X] 1 - List all products.
- [X] 2 - Stock products with low stock - Update.
- [X] 3 - Enter new products to stock.
- [X] 4 - Search product by code.
- [X] 5 - Display the value for each stocked product.
- [X] 6 - Consult stock products released for sales promotion.
- [X] 7 - Quit APP and save changes.

#### 4.1 List all products.
Tabulates the inventory.txt data in an easy to read format:

<img src="https://user-images.githubusercontent.com/81885034/220939327-d3d3cf44-598f-4f49-841b-3b2c1128b481.png" height="600"/>


#### 4.2 Stock products with low stock - Update.

It displays and returns (1 product at a time) the products and the amount of items with less stock,<br /> 
then prompts the user to enter the desired quantity for replenishment.

If the user enters an amount for the restock, then the item is updated and moves to another product<br /> 
with low inventory until the user clicks 0 to exit.

<img src="https://user-images.githubusercontent.com/81885034/220946477-f7cef79a-35c2-405d-ab56-b30fa7acfa9b.png" height="500"/>

#### 4.3 Enter new products to stock.
Gives a series of requests for the user to enter the data for each field in a new product entry<br /> 
to be added to inventory.py

<img src="https://user-images.githubusercontent.com/81885034/220952129-912b35d6-7ea8-415e-a1f2-7fc0ffde48ae.png" height="480"/>

*Please note that 'Value' and 'Quantity' must be provided as numbers, otherwise<br /> 
an error message will appear.*

#### 4.4 Search product by code.

Allows user to enter a prefixed product code starting with 'SKU' to search for<br /> 
a product in inventory.txt

<img src="https://user-images.githubusercontent.com/81885034/220965435-87492ce6-9d55-419c-b592-88e33f32d9be.png" height="420"/>

#### 4.5 Display the value for each stocked product.

Calculates the total value of each product (Value multiplied by quantity).<br />
Displays this information in an easy-to-read table.

<img src="https://user-images.githubusercontent.com/81885034/220971249-07d9fc4b-ff49-43da-b6aa-b02946f6840a.png" height="650"/>

#### 4.6 Consult stock products released for sales promotion.

Returns the quantity and model of the product with the largest number of items in stock.<br />
Displays the message that the product is released in one of the countries where the<br /> 
deposit is located.

<img src="https://user-images.githubusercontent.com/81885034/220977824-8c167ea3-6c49-45b7-a501-f3de0d8f4b7b.png" height="370"/>



#### 4.7 Quit APP and save changes.

Closes the program.

---

### 5) Reference.

Task performed by software engineering student Eleandro S. Joaquim, using a task<br /> 
model from the Bootcamp [HyperionDev](hyperiondev.com) course.

Materials in .pdf format Tasks 34, 35 and 36 provided by the school [HyperionDev](hyperiondev.com)

---


