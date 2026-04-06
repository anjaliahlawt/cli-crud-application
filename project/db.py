import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")


try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password, 
    )
    cursor = connection.cursor()

 
    cursor.execute("CREATE DATABASE IF NOT EXISTS crud_app")
    cursor.execute("USE crud_app")
    print("Database connected successfully")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        address VARCHAR(255),
        contact BIGINT,
        deleted BOOLEAN DEFAULT FALSE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        taskid INT AUTO_INCREMENT PRIMARY KEY,
        customer_id INT,
        title VARCHAR(100),
        status ENUM('pending','done'),
        priority ENUM('low','medium','high'),
        deadline DATE,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
    """)

    print("Tables are created successfully")

except mysql.connector.Error as err:
    print(" Error:", err)


