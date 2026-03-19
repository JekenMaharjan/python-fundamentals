# ==========================================================================================
# Python simple hello world
# ==========================================================================================

print("Hello World!\n")

# ==========================================================================================
# Variables
# ==========================================================================================

print("This is My Details:")

name = "Jeken Maharjan"
age = 25
weight = 105

print("My name is " + name + ".")
print(f"I am {age} Years Old.")
print(f"I weight {weight} kg\n")

# ==========================================================================================
# Data Types
# ==========================================================================================

# 1. String (Text)
one_name = "Jeken"

# 2. Integer (Whole numbers)
age = 25

# 3. Float (Decimal numbers)
price = 19.99

# 4. Boolean (True / False)
is_student = True

# ==========================================================================================
# Taking Input from User
# ==========================================================================================

full_name = input("Enter your fullname: ")
print(f"Your fullname is {full_name}.\n")

# ==========================================================================================
# Simple Math Operations
# ==========================================================================================

a = 10
b = 5

print(f"Addition: {a + b}")  # addition
print(f"Subtraction: {a - b}")  # subtraction
print(f"Multiplication: {a * b}")  # multiplication
print(f"Division: {int(a / b)}\n")  # division

# ==========================================================================================
# If Condition
# ==========================================================================================

age = 18

if age >= 18:
    print("You are an adult.\n")

# ==========================================================================================
# For Loop
# ==========================================================================================

for i in range(5):
    print(i)

# ==========================================================================================
# Lists (Very Important)
# ==========================================================================================

numbers = [1,2,3,4,5]

print(f"\n{numbers}")

print(f"\nIndex 0 of given list is {numbers[0]}")
print(f"Index 1 of given list is {numbers[1]}")
print(f"Index 2 of given list is {numbers[2]}")
print(f"Index 3 of given list is {numbers[3]}")
print(f"Index 4 of given list is {numbers[4]}\n")

# ==========================================================================================
# Function
# ==========================================================================================

def add(a,b):
    return a + b

print(f"Result of function add is {add(5,3)}\n")

# ==========================================================================================
# Add numbers from a list.
# ==========================================================================================

def add_list(numbers):
    total = 0
    
    for num in numbers:
        total += num
        
    return total
    
print(f"Addition of numbers from a given list is {add_list([1,2,3,4])}\n")

# ==========================================================================================
# Lists (Core Data Structure)
# ==========================================================================================

numbers_two = [10, 20, 30, 40]

numbers_two.append(50)     # add element
numbers_two.remove(20)     # remove element
print(f"Length of given list is {len(numbers_two)}\n")    # length

for num in numbers_two:
    print(num)
    
print()

# ==========================================================================================
# Dictionaries (VERY IMPORTANT)
# ==========================================================================================

user = {
    "name": "Jeken",
    "age": 24,
    "is_student": False
}

print(f"Username : {user['name']}")
print(f"Age : {user['age']}")
print(f"Is user Student? : {user['is_student']}")

print() # adds one blank line

for key, value in user.items():
    print(key, value)
    
print()

# ==========================================================================================
# Functions (Reusable Logic)
# ==========================================================================================

def greet(name):
    return "Hello " + name

print(greet("Jeken"))

print()

# ==========================================================================================
# Working with Files (Very Practical)
# ==========================================================================================

# Write to file
with open("data.txt", "w") as file:
    file.write("Hello World")
    
# Read file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    
# ==========================================================================================
# Basic Exception Handling (Avoid Crashes)
# ==========================================================================================

try:
    num = int("abc")
except:
    print("Error occurred")
    
# ==========================================================================================
# Working with APIs (Python Version)
# ==========================================================================================

import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()

for user in data:
    print(user["name"])
    
# ==========================================================================================
# Simple Real-World Mini Example
# ==========================================================================================

import requests

def get_users():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    return res.json()

users = get_users()

for user in users:
    print(user["name"])