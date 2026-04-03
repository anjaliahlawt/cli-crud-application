import json
from datetime import datetime

customers = []
unique_id = 0

tasks = []
task_id = 0


# customers data from file


def load_data():
    global customers, unique_id

    try:
        with open("crud.json", "r") as file:
            data = json.load(file)
            customers = data["customers"]

        if customers:
            unique_id = customers[-1]["id"]
        else:
            unique_id = 0

    except:
        customers = []
        unique_id = 0


# tasks data from file
def load_tasks():
    global tasks, task_id

    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)
            tasks = data["tasks"]

        if tasks:
            task_id = tasks[-1]["taskid"]
        else:
            task_id = 0

    except:
        tasks = []
        task_id = 0


# save customers data to file


def save_data():
    with open("crud.json", "w") as file:
        json.dump({"customers": customers}, file)


# save tasks data to file


def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump({"tasks": tasks}, file)


# customers  id generate


def id_generate():
    global unique_id
    unique_id += 1
    return unique_id


# tasks id generate


def task_id_generate():
    global task_id
    task_id += 1
    return task_id


# Add customer with validation


def add_customer():
    global customers

    cid = id_generate()

    while True:
        name = input("Enter name: ")
        if name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid name")

    while True:
        email = input("Enter email: ")
        if email.count("@") == 1 and email.endswith("@gmail.com"):
            break
        else:
            print("Invalid email")

    while True:
        address = input("Enter address: ")
        if address.replace(" ", "").isalnum():
            break
        else:
            print("Invalid address")

    while True:
        contact = input("Enter contact: ")
        if contact.isdigit() and len(contact) == 10:
            break
        else:
            print("Invalid contact")

    customer = {
        "id": cid,
        "name": name,
        "email": email,
        "address": address,
        "contact": contact,
        "deleted": False,
    }

    customers.append(customer)

    print("Customer added successfully")
    save_data()


# show customer


def show_customer():
    cid = int(input("Enter ID: "))

    for c in customers:
        if c["id"] == cid and not c["deleted"]:

            print("Name:", c["name"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            print("Contact:", c["contact"])
            print("Deleted:", c["deleted"])
            return

        print("Customer not found")


# show all customers

def showall_customer():
    for c in customers:
        if not c["deleted"]:
            print("Id :", c["id"])
            print("Name:", c["name"])
            print("Email:", c["email"])
            print("Address:", c["address"])
            print("Contact:", c["contact"])
            print("Deleted:", c["deleted"])

        print("-" * 20)


# update customer

def update_customer():
    cid = int(input("Enter customer ID: "))

    for c in customers:
        if c["id"] == cid and not c["deleted"]:

            print("Leave blank if you don't want to change")

            # name
            while True:
                name = input("Enter name: ")
                if name == "" or name.replace(" ", "").isalpha():
                    break
                else:
                    print("Invalid name")

            # email
            while True:
                email = input("Enter email: ")
                if email == "" or (email.count("@") == 1 and email.endswith("@gmail.com")):
                    break
                else:
                    print("Invalid email")

            # address
            while True:
                address = input("Enter address: ")
                if address == "" or address.replace(" ", "").isalnum():
                    break
                else:
                    print("Invalid address")

            # contact
            while True:
                contact = input("Enter contact: ")
                if contact == "" or (contact.isdigit() and len(contact) == 10):
                    break
                else:
                    print("Invalid contact")

            
            if name != "":
                c["name"] = name
            if email != "":
                c["email"] = email
            if address != "":
                c["address"] = address
            if contact != "":
                c["contact"] = contact

            save_data()
            print("Customer updated successfully")
            return

    print("Customer not found")

# Delete customer


def delete_customer():
    cid = int(input("Enter customer ID: "))

    for c in customers:
        if c["id"] == cid and not c["deleted"]:

            c["deleted"] = True
            save_data()
            print("Customer deleted successfully")
            return

    print("Customer not found")


# Add task


def add_task():
    cid = int(input("Enter customer ID: "))

    for c in customers:
        if c["id"] == cid and not c["deleted"]:
            break
    else:
        print("Customer not found")
        return

    taskid = task_id_generate()

    while True:
        title = input("Enter task title: ")
        if title.replace(" ", "").isalpha():
            break
        else:
            print("Invalid title (letters only)")

    while True:
        status = input("Enter status (pending/done): ")
        if status == "pending" or status == "done":
            break
        else:
            print("Invalid status")

    while True:
        priority = input("Enter priority (low/medium/high): ")
        if priority in ["low", "medium", "high"]:
            break
        else:
            print("Invalid priority")

    while True:
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        try:
            datetime.strptime(deadline, "%d-%m-%Y")
            break
        except:
            print("Invalid date format")

    task = {
        "taskid": taskid,
        "customer_id": cid,
        "title": title,
        "status": status,
        "priority": priority,
        "deadline": deadline,
    }

    tasks.append(task)
    save_tasks()

    print("Task added successfully")


# show tasks

def show_tasks():
    cid = int(input("Enter customer ID: "))

    # 🔍 check customer exist
    for c in customers:
        if c["id"] == cid and not c["deleted"]:
            break
    else:
        print("Customer not found")
        return

    
    count = 0

    for t in tasks:
        if t["customer_id"] == cid:
            print("Task ID:", t["taskid"])
            print("Title:", t["title"])
            print("Status:", t["status"])
            print("Priority:", t["priority"])
            print("Deadline:", t["deadline"])
            print("-" * 20)
            count += 1

    if count == 0:
        print("No tasks")

# show all task

def show_all_tasks():
    if not tasks:
        print("No tasks found")
        return

    for t in tasks:
        print("Task ID:", t["taskid"])
        print("Customer ID:", t["customer_id"])
        print("Title:", t["title"])
        print("Status:", t["status"])
        print("Priority:", t["priority"])
        print("Deadline:", t["deadline"])
        print("-" * 20)


load_data()
load_tasks()

choice = 1
while choice != 9:
    print("1. Add customer")
    print("2. Show customer")
    print("3. Show all customers")
    print("4. Update customer")
    print("5. Delete customer")
    print("6. Add task")
    print("7. Show tasks")
    print("8. Show all tasks")
    print("9. Exit")
    try:
        choice = int(input("enter your choice: "))
    except:
        print("invalid input enter the digits only")
        continue

    if choice == 1:
        add_customer()
    elif choice == 2:
        show_customer()
    elif choice == 3:
        showall_customer()
    elif choice == 4:
        update_customer()
    elif choice == 5:
        delete_customer()
    elif choice == 6:
        add_task()
    elif choice == 7:
        show_tasks()
    elif choice == 8:
        show_all_tasks()
    elif choice == 9:
        break
    else:
        print("invalid choice")
