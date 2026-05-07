"""
Session: Five
Date: 2nd May 2026 11:30am-1pm
focus: Setup (if, else, elif)
Facilitator: Olatunbosun
"""
# Hard coded variable
name = 'Samuel Gregory'
age = 32
dept = "Mass Communication"
hobby = 'Football'
height= 1.67

print("\n------Hard Coded Variables--------")
print("Hi, am ",name, "\n")

# Dynamic Variables
# name = str(input("Please your full name: "))
# print("\n------Dynamic Variable--------")
# print("Hi, am ", name)

# # Printing ID card for Samuel
# print("\n---------Mautech Student ID Card Option1-------------")
# print("Fullname:", name,".")
# print("Age:     ", age)
# print("Dept:", dept)
# print("Hobby:", hobby)
# print("This Card is the property of MAU")
# print("-"*50)

# print("\n---------Mautech Student ID Card Option2-------------")
# print("Fullname:", name,"\nAge:     ", age,"\nDept:", dept, "\nHobby:",hobby,"\nThis card is the property of MAU\n", "-"*50)


# IF Statement
"""
If statement worked on simple logic of yes or no. 
Only one option can be true at a time. two can conditions can not be valid.
"""

# marv =  float(input("Marv age in number please: "))
# greg = float(input("Greg age in number please: "))
# sam = float(input("Sam age in number please: "))

# # if only without considering the opposite result
# if marv>greg:
#     print(f"\nComparing ages result show that Marve is Older at {int(marv)} \n")

# # # if/else
# # if marv>greg:
# #     print("\nComparing ages result show that Marve is Older \n")
# else:
#     print("\nComparing ages result show that Greg is Older \n")


# # if/elif/else
# if marv>greg:
#     print("\nComparing ages result show that Marve is Older than Greg \n")
# elif marv>sam:
#     print("\nComparing ages result show that Sam is Older than Marv \n")
# elif greg>sam:
#     print("\nComparing ages result show that Greg is the youngest \n")
# else:
#     print("invalid Statement")


# Calculator
amount = float(input("Enter the total purchase amount naira: "))
discount_rate = 0.0
if amount >= 120000:
    discount_rate = 0.09
    print("Status: 10% Gold Discount Applied")
elif amount >= 60000:
    discount_rate = 0.04
    print("Status: 5% Silver Discount Applied")
else:
    discount_rate = 0.0
    print("Status: No Discount Applied")

discount_value = amount * discount_rate
subtotal = amount - discount_value
tax_rate = 0.075
tax_amount = subtotal * tax_rate

total_final = subtotal + tax_amount

print("\n      Amiral Store")
print("-" * 30)
print(f"Original Amount: {amount:,.2f}")
print(f"Discount:       -{discount_value:,.2f}")
print(f"Subtotal:        {subtotal:,.2f}")
print(f"VAT (7.5%):     +{tax_amount:,.2f}")
print("-" * 30)
print(f"TOTAL PAYABLE:   {total_final:,.2f}")
print("\n Any goods sold can not be return")
print("-" * 30)