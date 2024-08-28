# You are tasked with creating a simple inventory management system for a market. The system should allow users to add, update, view, and remove items from the inventory. Each item in the inventory will have a name, price, quantity, and category.

# Functionality:

# Add Item: Create a function add_item that allows users to add a new item to the inventory. Users should input the name, price, quantity, and category of the item.

# Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory. Users should be able to update the price, quantity, and category of the item.

# View Inventory: Develop a function view_inventory that displays all items in the inventory along with their details (name, price, quantity, and category).
# Remove Item: Create a function remove_item that allows users to remove an item from the inventory based on its name.

# Search by Category: Implement a function search_by_category that allows users to search for items in the inventory based on their category. The function should display all items belonging to the specified category.

# Project Structure:
# Define a list inventory to store the items in the market inventory. Each item should be represented as a dictionary with keys for name, price, quantity, and category.

# Implement the functions add_item, update_item, view_inventory, remove_item, and search_by_category to manage the inventory.

# Create a main loop to interact with the user. The loop should prompt the user to choose from various options such as adding, updating, viewing, removing items, or searching by category.

# Research dictionaries:
# https://www.w3schools.com/PYTHON/python_dictionaries.asp
# thisdict = {
#  "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Python Dictionaries

# thisdict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# Dictionaries are written with curly brackets, and have keys and values:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# Project Structure: Define a list inventory to store the items in the market inventory.
# Each item should be represented as a dictionary with keys for name, price, quantity, and category.

inventory = []


# Add Item: Create a function add_item that allows users to add a new item to the inventory.
# Users should input the name, price, quantity, and category of the item.

def add_item():
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    quantity = int(input("Enter the item quantity: "))
    category = input("Enter the item category: ")

    item = {
        'name': name,
        'price': price,
        'quantity': quantity,
        'category': category
    }

    inventory.append(item)
    # confirm item was added, audit trail
    print("\nItem added")
    print(f"Name: {item['name']}")
    print(f"Price: ${item['price']:.2f}")
    print(f"Quantity: {item['quantity']}")
    print(f"Category: {item['category']}")
    print()

# Update Item: Implement a function update_item that allows users to update the details of an existing item in the inventory.
# Users should be able to update the price, quantity, and category of the item.

def update_item():
    name = input("Enter the name of the item to update: ")
    for item in inventory:
        if item['name'] == name: # watch error handling
            print(f"Updating item '{name}':")
            item['price'] = float(input("Enter the new price: "))
            item['quantity'] = int(input("Enter the new quantity: "))
            item['category'] = input("Enter the new category: ")
            print(f"Item '{name}' updated successfully!")
            return
    print(f"Item '{name}' not found in inventory.")

# View Inventory: Develop a function view_inventory that displays all items in the inventory
# along with their details (name, price, quantity, and category).

def view_inventory():
# need to mnake sure inventory is populated?
    if not inventory:
        print("The inventory is empty.")
        return
    print("\nInventory:")
    for item in inventory:
        print(f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}, Category: {item['category']}")
    print()


# Remove Item: Create a function remove_item that allows users to remove
# an item from the inventory based on its name.

# Research: why doesn't remove_item work but add_item does? Need "global" in remove_item:
# Since you are reassigning the inventory variable to a new list, Python needs to know that
# this inventory refers to the global variable, not a local one. The global keyword is required to modify the
# global variable rather than creating a new local variable with the same name.
# This is *different from appending in add_item.

def remove_item():
    name = input("Enter the name of the item to remove: ")
    global inventory
    inventory = [item for item in inventory if item['name'] != name]

    print(f"Item '{name}' removed from inventory.")


# Search by Category: Implement a function search_by_category that allows users to search for items
# in the inventory based on their category.
# The function should display all items belonging to the specified category (test: multiple items in a category).

def search_by_category():
    category = input("Enter the category to search: ")
    found_items = [item for item in inventory if item['category'] == category]
    if not found_items:
        print(f"No items found in category '{category}'.")
        return

    print(f"\nItems in category '{category}':")
    for item in found_items:
        print(f"Name: {item['name']}, Price: ${item['price']:.2f}, Quantity: {item['quantity']}")
    print()


# Create a main loop to interact with the user. The loop should prompt the user to choose from various options
# such as adding, updating, viewing, removing items, or searching by category.
# Watch exiting loop
def main():
    print("Select an action from the Inventory Management System menu:")
    while True:
        print("1. Add Item")
        print("2. Update Item")
        print("3. View Inventory")
        print("4. Remove Item")
        print("5. Search by Category")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            update_item()
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            remove_item()
        elif choice == '5':
            search_by_category()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# research: how to execute main, with help from ChatGPT
# The if __name__ == "__main__": construct is used to ensure that code is executed
# only when a script is run directly and not when it is imported as a module.
if __name__ == "__main__":
    main()