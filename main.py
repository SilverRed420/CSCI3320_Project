import os

FILE_NAME = "coffee_inventory.txt"

def add_coffee():
    coffee_name = input("Enter the name of the coffee: ")
    coffee_weight = input("Enter the weight of the coffee (in lbs): ")
    with open(FILE_NAME, "a") as file:
        file.write(coffee_name+","+coffee_weight+"\n")
    print(f"Coffee '{coffee_name}' added successfully.")

def display_coffees():
    with open(FILE_NAME, "r") as file:
        coffees = file.readlines()
        if not coffees:
            print("No coffees found.")
            return
        print("Coffee Inventory:")
        for coffee in coffees:
            name, weight = coffee.strip().split(",")
            print(f"Name: {name}, Weight: {weight} lbs")

def modify_coffee():
    # Ask the user for the coffee name to modify
    display_coffees()
    coffee_name = input("Enter the name of the coffee to modify: ")
    #read the existing coffees from the file
    with open(FILE_NAME, "r") as file:
        coffees = file.readlines()
    # Open the file in write mode to overwrite it with modified data
    with open(FILE_NAME, "w") as file:
        found = False

        for coffee in coffees:
            name, weight = coffee.strip().split(",")
            # Check if the current coffee name matches the one to modify
            if name == coffee_name:

                new_name = input(f"Enter the new name for '{name}' (or press Enter to keep it the same): ")
                if not new_name:
                    new_name = name
                
                new_weight = input(f"Enter the new weight for '{name}' (in lbs): ")
                file.write(f"{new_name},{new_weight}\n")
                found = True
                print(f"Coffee '{name}' modified successfully.")
                
            else:
                file.write(coffee)
        if not found:
            print(f"Coffee '{coffee_name}' not found.")

def delete_coffee():
    # Show the current inventory so the user can pick a record
    display_coffees()
    coffee_name = input("Enter the name of the coffee to delete: ")
    # Read the existing coffees from the file
    with open(FILE_NAME, "r") as file:
        coffees = file.readlines()
    found = False
    # Rewrite the file, skipping the record that matches the name
    with open(FILE_NAME, "w") as file:
        for coffee in coffees:
            name, weight = coffee.strip().split(",")
            if name == coffee_name:
                found = True
            else:
                file.write(coffee)
    if found:
        print(f"Coffee '{coffee_name}' deleted successfully.")
    else:
        print(f"Coffee '{coffee_name}' not found.")

def search_coffee():
    search_name = input("Enter the name of the coffee to search for: ")
    with open(FILE_NAME, "r") as file:
        coffees = file.readlines()
    found = False
    for coffee in coffees:
        name, weight = coffee.strip().split(",")
        # Case-insensitive match on the description
        if name.lower() == search_name.lower():
            print(f"Found - Name: {name}, Weight: {weight} lbs")
            found = True
    if not found:
        print(f"Coffee '{search_name}' not found.")


def display_options():
    print("\nCoffee Inventory Management System\n")
    print("Choose one of the following options 1-6:")
    print("1. Add a new coffee")
    print("2. Display all coffees")
    print("3. Modify a coffee")
    print("4. Delete a coffee")
    print("5. Search for a coffee")
    print("6. Exit")

def main():

    if os.path.exists("coffee_inventory.txt"):
        print("file opened successfully")
    else:
        print("file not found")
        with open("coffee_inventory.txt", "w") as file:
            print("file created successfully")

    while True:
        display_options()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_coffee()
        elif choice == '2':
            display_coffees()
        elif choice == '3':
            modify_coffee()
        elif choice == '4':
            delete_coffee()
        elif choice == '5':
            search_coffee()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




main()
