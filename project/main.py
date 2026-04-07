
from db import connection, cursor
from datetime import datetime

#add customer

def add_customer():
    
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
            print("Invalid email @gmail.com")

    
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
            print("Invalid contact 10 digits.")

    
    query = "INSERT INTO customers (name, email, address, contact) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, email, address, contact))
    connection.commit()
    print("Customer added successfully")


#show customer

def show_customer(cid):
    cursor.execute("SELECT * FROM customers WHERE id=%s AND deleted=FALSE", (cid,))
    customer = cursor.fetchone()
    if customer:
        print(customer)
    else:
        print("Customer not found")

#show all customers

def showall_customers():
    cursor.execute("SELECT * FROM customers WHERE deleted=FALSE")
    data = cursor.fetchall()
    for c in data:
        print(c)


#update customer

def update_customer(cid):

    cursor.execute("SELECT * FROM customers WHERE id=%s AND deleted=FALSE", (cid,))
    customer = cursor.fetchone()

    if not customer:
        print("Customer not found or already deleted ")
        return  

    print("Leave blank to skip")

    
    while True:
        name = input("Enter name: ")
        if name == "":
            name = customer[1]
            break
        elif name.replace(" ", "").isalpha():
            break
        else:
            print("Invalid name")

    
    while True:
        email = input("Enter email: ")
        if email == "":
            email = customer[2]
            break
        elif email.count("@") == 1 and email.endswith("@gmail.com"):
            break
        else:
            print("Invalid email")

    
    while True:
        address = input("Enter address: ")
        if address == "":
            address = customer[3]
            break
        elif address.replace(" ", "").isalnum():
            break
        else:
            print("Invalid address")

    
    while True:
        contact = input("Enter contact: ")
        if contact == "":
            contact = customer[4]
            break
        elif contact.isdigit() and len(contact) == 10:
            break
        else:
            print("Invalid contact")

    
    query = """
    UPDATE customers 
    SET name=%s, email=%s, address=%s, contact=%s 
    WHERE id=%s
    """

    cursor.execute(query, (name, email, address, contact, cid))
    connection.commit()

    print("Customer updated successfully")


#delete customer

def delete_customer(cid):
    cursor.execute("UPDATE customers SET deleted=TRUE WHERE id=%s",(cid,))
    connection.commit()
    print("Customer deleted!")




#add task

def add_task(cid):

    cursor.execute("SELECT * FROM customers WHERE id=%s AND deleted=FALSE", (cid,))
    if not cursor.fetchone():
     print("Customer not found")
     return
    title = input("Title: ")
    
    
    while True:
        status = input("Status (pending/done): ")
        if status in ["pending", "done"]:
            break
        else:
            print("Invalid status")

    
    while True:
        priority = input("Priority (low/medium/high): ")
        if priority in ["low", "medium", "high"]:
            break
        else:
            print("Invalid priority")


    while True:
        deadline = input("Deadline YYYY-MM-DD: ")
        try:
            datetime.strptime(deadline, "%Y-%m-%d")
            break
        except:
            print("Invalid date format")

    query = """
    INSERT INTO tasks (customer_id,title,status,priority,deadline) 
    VALUES (%s,%s,%s,%s,%s)
    """

    cursor.execute(query,(cid,title,status,priority,deadline))
    connection.commit()

    print("Task added successfully")


#show task 

def show_tasks(cid):
    cursor.execute("SELECT * FROM tasks WHERE customer_id=%s",(cid,))
    data = cursor.fetchall()
    for t in data:
        print(t)


#show all task

def showall_tasks():
    cursor.execute("SELECT * FROM tasks")
    data = cursor.fetchall()
    for t in data:
        print(t)





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

    if choice==1:
        add_customer()
    elif choice==2:
        show_customer(int(input("Customer ID: ")))
    elif choice==3:
        showall_customers()
    elif choice==4:
       update_customer(int(input("Customer ID: ")))
    elif choice==5:
        delete_customer(int(input("Customer ID: ")))
    elif choice==6:
        add_task(int(input("Customer ID: ")),)
    elif choice==7:
        show_tasks(int(input("Customer ID: ")))
    elif choice==8:
        showall_tasks()
    elif choice==9:
        break
    else:
        print("Invalid choice")