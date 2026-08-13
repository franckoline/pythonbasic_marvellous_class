import random
import json

#initializing variables
employees = {}
names = []
initials = []
unique_ID = []
file_path = "employees.json"

# getting total number of employees
while True:
    try:
        num_of_employees = int(input("Enter number of employees: "))
        if num_of_employees <= 0:
            print("Number of employees must be greater than 0")
            continue
        break
    except ValueError:
        print("Please enter a valid whole number.")

# getting names of each employee
i = 0
while i < num_of_employees:
    name = input(f"Enter the name of employee no. {i + 1}: ").strip()
    if name == "":
        print("Name cannot be empty.")
        continue
    if name.isdigit():
        print("Name cannot contain digits")
        continue
    names.append(name)
    initials.append(name[0].upper())
    i += 1

# Generating random numbers for the employee ID and creating their unique ID
IDs = list(random.sample(range(2210, 2210 + num_of_employees), num_of_employees))
for i in range(num_of_employees):
    ids = f"{initials[i]}000{IDs[i]}"
    unique_ID.append(ids)

# Printing the unique ID for each employee
print("\n")
for i in range(num_of_employees):
    print(f"The unique ID for {names[i]} is {unique_ID[i]}")

# Storing the names and ID of each employee in a dictionary and saving it into json file
for i in range(num_of_employees):
    employees[f"{names[i]}"] = f"{unique_ID[i]}"
try:
    with open(file_path, "w") as file:
       json.dump(employees, file, indent = 4)
except FileExistsError:
    print("This file already exist.")
