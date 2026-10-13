import os

FILE_NAME = "example.txt"

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

def display_options():
    print("Coffee Inventory Management System\n")
    print("Choose one of the following options 1-6:")
    print("1. Add a new coffee")
    print("2. Display all coffees")
    print("3. Modify a coffee")
    print("4. Delete a coffee")
    print("5. Search for a coffee")
    print("6. Exit")

def main():

    with open("coffee_inventory.txt", "r") as file:
        print("file opened successfully")

    while True:
        display_options()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("Add a new coffee functionality goes here.")
            # Add code to add a new coffee
        elif choice == '2':
            print("Display all coffees functionality goes here.")
            # Add code to display all coffees
        elif choice == '3':
            print("Modify a coffee functionality goes here.")
            # Add code to modify a coffee
        elif choice == '4':
            print("Delete a coffee functionality goes here.")
            # Add code to delete a coffee
        elif choice == '5':
            print("Search for a coffee functionality goes here.")
            # Add code to search for a coffee
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




main()
