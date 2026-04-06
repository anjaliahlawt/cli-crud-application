# CRUD operation for file

filename = "file.txt"

# Add data
def add_data():
    data = input("Enter data to add")
    with open(filename, "a") as file:
        file.write(data)
    print("Data added successfully")

# Read data
def read_data():
    try:
        with open(filename, "r") as file:
            print(file.read())
    except:
        print("File not found!")

# Update data

def update_data():
    print("1. Overwrite data")
    print("2. Append data")
    
    choice = input("Enter choice")

    if choice == "1":
        new_data = input("Enter new data: ")
        with open(filename, "w") as file:
            file.write(new_data + "\n")
        print("File overwritten successfully!")

    elif choice == "2":
        new_data = input("Enter data to append: ")
        with open(filename, "a") as file:
            file.write(new_data + "\n")
        print("Data appended successfully!")

    else:
        print("Invalid choice!")

# Delete data 

def delete_data():
    with open(filename, "w") as file:
        file.write("")
    print("Data deleted successfully!")


while True:
    print("\n1. Add data")
    print("2. Read data")
    print("3. Update data")
    print("4. Delete data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_data()
    elif choice == 2:
        read_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        break
    else:
        print("Invalid choice!")