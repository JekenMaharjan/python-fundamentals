# Student Record System

import mysql.connector
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Step 1: Connect (no DB)
conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS student_record_system_db")
print("Database Created Successfully!")

# Close first connection
cursor.close()
conn.close()

# Step 2: Connect to MySQL
conn = mysql.connector.connect(
    host = os.getenv("DB_HOST"),
    user = os.getenv("DB_USER"),
    password = os.getenv("DB_PASSWORD"),
    database = os.getenv("DB_NAME")
)

cursor = conn.cursor()
print("Connected to Student Record System Database!")

print(" ")

# Main menu
while True:
    print("\nWELCOME TO STUDENT RECORD SYSTEM FOR MATHS")
    print(" ")
    print("1. Add student")
    print("2. Show all students")
    print("3. Update marks")
    print("4. Show top students")
    print("5. Delete student")
    print("6. Exit")

    print(" ")

    # Create students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100) NOT NULL,
        marks INT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Choice to operate this system
    choice = input("Enter choice: ")

    print(" ")

    # Choices
    # 1. Add student
    if choice == "1":
        print("ADD STUDENT:")
        
        try:
            name = input("Enter name: ")
            marks = int(input("Enter marks: "))
        except  ValueError:
            print("Invalid Input! Operation cancelled.")
            continue  # Go back to menu
        
        cursor.execute("INSERT INTO students (name, marks) VALUES (%s, %s)", (name, marks))
        conn.commit()
        print("New student added!")
        
    # 2. Show all students
    elif choice == "2":
        print("ALL STUDENT:")
        
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        
        if not students:
            print("No students found...")
        else:
            # Header
            print("-" * 50)
            print(f"{'ID':<5} {'Name':<20} {'Marks':<5}")
            print("-" * 50)

            # Data
            for student in students:
                print(f"{student[0]:<5} {student[1]:<20} {student[2]:<5}")

    # 3. Update marks
    elif choice == "3":
        print("UPDATE STUDENT:")
        
        try:
            id = int(input("Enter student id: "))
            marks = int(input("Enter updated marks: "))
        except ValueError:
            print("Invalid Input! Operation cancelled.")
            continue  # Go back to menu
        
        cursor.execute("UPDATE students SET marks = (%s) WHERE id = (%s)", (marks, id))
        conn.commit()
        
        if cursor.rowcount > 0:
            print("Updated successfully!")
        else:
            print("Student not found!")

    # 4. Show top students
    elif choice == "4":
        print("TOP 3 STUDENTS:")
        
        cursor.execute("SELECT * FROM students ORDER BY marks DESC LIMIT 3")
        students = cursor.fetchall()
        
        if not students:
            print("No students found...")
        else:
            # Header
            print("-" * 50)
            print(f"{'ID':<5} {'Name':<20} {'Marks':<5}")
            print("-" * 50)

            # Data
            for student in students:
                print(f"{student[0]:<5} {student[1]:<20} {student[2]:<5}")

    # 5. Delete student
    elif choice == "5":
        print("DELETE STUDENT:")
        
        try:
            id = int(input("Enter the id of Student that you want to delete: "))
        except ValueError:
            print("Invalid Input! Operation cancelled.")
            continue  # Go back to menu
        
        cursor.execute("DELETE FROM students WHERE id = (%s)", (id,))
        conn.commit()
        print("Deleted student Successfully!")

    # 6. Exit
    elif choice == "6":
        print("Exiting...")
        break

    # Invalid choice
    else:
        print("Invalid choice!")

# Close connection
cursor.close()
conn.close()

