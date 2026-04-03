Customer & Task Management System (Python CLI)

Description

This is a Command Line Interface (CLI) based project built using Python.
It allows you to manage customers and their tasks with full CRUD operations.

Data is stored using JSON files, so it persists even after restarting the program.

->Features
 1.Customer Management
 Add new customer
 View single customer
 View all customers
 Update customer details
 Soft delete customer (mark as deleted)
2. Task Management
Add task for a customer
View tasks of a specific customer
View all tasks
Task includes:
Title
Status (pending/done)
Priority (low/medium/high)
Deadline

3.Technologies Used
Python
JSON (for data storage)
datetime module

4.Validations Implemented
Name → Only alphabets allowed
Email → Must be in @gmail.com format
Contact → Must be 10 digits
Deadline → Format DD-MM-YYYY
