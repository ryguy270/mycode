#!/usr/bin/env python3
# Define a list to store items
items = []

# Function to create an item
def create_item():
    item = input("Enter the item to add: ")
    items.append(item)
    print("Item added successfully!")

# Function to read all items
def read_items():
    print("Items in the list:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

# Function to update an item
def update_item():
    read_items()
    try:
        index = int(input("Enter the index of the item to update: ")) - 1
        if 0 <= index < len(items):
            new_item = input("Enter the updated item: ")
            items[index] = new_item
            print("Item updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Function to delete an item
def delete_item():
    read_items()
    try:
        index = int(input("Enter the index of the item to delete: ")) - 1
        if 0 <= index < len(items):
            deleted_item = items.pop(index)
            print(f"{deleted_item} has been deleted.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

# Main loop
while True:
    print("\nMenu:")
    print("1. Add item")
    print("2. Read items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_item()
    elif choice == "2":
        read_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")