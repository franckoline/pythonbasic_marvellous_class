"""
Session: three
Date: 12th May 2026 09:30am-11:30pm
focus: Data Variables, Data Types, and Nested If Statements
Facilitator: Elvis
"""
#This was a class exercise based on workdone in nestedIf.py, it was dropped on the classroom
Business_name = str(input("What is the name of your business : "))
Owner_name = str(input("What is your name : "))
Owner_age = int(input("How old are you? : "))
Business_type = str(input("What type of business do you run? : "))
Country = str(input("Which country do you operate in? : "))
Monthly_revenue = int(input("What is your monthly revenue? : "))
Number_of_employees = int(input("How many employees do you have? : "))
Years_in_operation = int(input("How many years have you been in operation? : "))
is_registered = str(input("Is your business registered? yes/no : "))
has_tax_id = str(input("Do you have a tax identification number? yes/no : "))


if Owner_age >= 18:
    print("You are eligible for this operation. ")
print("You are not eligible for this operation. ")    

if Monthly_revenue < 50000 and Business_name >= 2:
    if is_registered and has_tax_id:
        print("Congratulations,Your Business qualifies for a government grants")