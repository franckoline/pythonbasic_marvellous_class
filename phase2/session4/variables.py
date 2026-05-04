"""
Session: One
Date: 2nd May 2026 11:30am-1pm
focus: setup (if, else, elif)
Facilitator: Marvellous
"""
# Hard coded Variable
'''Name = 'Marvellous Aguwa'
Age = 20
Dept = 'software engr'
Hobby = "football"
height = 4.67
print("\n------Hard Coded Variables------")
print("Hi, am "name, "\n")

# Dynamic Variables
name = str(input("Please yur full name"))
print("\n------Dynamic Variable------")
print("Hi, am ", name)

#Printing ID card for Marvellous
print("--------option 1--------")
print("\n--------Mewar Student ID Card--------")
print("Fullname: ", age)
print("dept: ",hobby )
print("\nThis card is the property of MIU\n")
print("-----------------------------------")

print("\n--------Mewar Student ID Card Option2--------")
print("Fullname,"\nAge: "" 
'''


# from itertools import count


# marv = float(input("marv age in number please: "))
# greg = float(input("greg age in number please: "))   
# sam  = float(input("sam age in numbetr please: ")) 


# if/elif/else
'''if marv<greg:
    print("\ncomparing ages results show that marv is older than greg \n")
elif marv<sam:
    print("\ncomparing ages results show that sam is older than marv \n")
elif greg<sam: 
    print("\ncomparing ages results show that greg is the youngest \n")
else:
    print("invalid statement")       
'''

# Calculator

amount = float(input("Enter the total purchase amount naira: "))

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

