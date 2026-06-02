#1.TYPING GAME
print("THE QUICK BROWN FOX JUMP OVER THE LAZY DOG.")

text = input("Type in the text above vert fast: ")

num = 1
while text != "THE QUICK BROWN FOX JUMP OVER THE LAZY DOG":
    text = input("Type in the text again: ")
    num = num + 1

print(f"CONGRATULATIONS.It took you {num} tries.")

#2.  Multi-function calculator
print("\n***CALCULATOR***")


print("1. +.")
print("2. -.")
print("3. *.")
print("4. /.")
print("5. Square root.")
operation = int(input("Select an operation: "))

if operation == 1:
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    answer = a + b
    print(f"The sum of {a} and {b} is {answer}.")
elif operation == 2:
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    answer = a - b
    print(f"The difference between {a} and {b} is {answer}.")
elif operation == 3:
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    answer = a * b
    print(f"The multiplication of {a} and {b} is {answer}.")
elif operation == 4:
    a = int(input("Input first number: "))
    b = int(input("Input second number: "))

    answer = a / b
    print(f"The division of {a} by {b} is {answer:.2f}.")
elif operation == 5:
    num = int(input("Input number: "))
    answer = pow(num, (1/2))
    print(f"The square root of {num} is {answer:.2f}.")
else:
    print("Invalid operation(Choose between 1 to 5).")

# 3. Recharge services
import time
print("\n***RECHARGE SERVICES***")


print("1. Buy airtime.")
print("2. Buy data.")
print("3. Check balance.")
print("4. Transfer airtime.")

balance = 1000
choice = int(input("Select an option: "))

if choice == 1:

   airtime = int(input("How much airtime do you want to purchase: "))
   if airtime <= balance:
      print("Processing your request...")
      time.sleep(1)
      print("1")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("3")
      time.sleep(1)
      print(f"You have successfully purchased {airtime}naira airtime.")
   else:
      print("Insufficient balance.")

elif choice == 2:
   data = int(input("How much data do you want to purchase: "))
   if data <= balance:
      print("Processing your request...")
      time.sleep(1)
      print("1")
      time.sleep(1)
      print("2")
      time.sleep(1)
      print("3")
      time.sleep(1)
      print(f"You have successfully purchased {data}naira worth of data.")
   else:
      print("Insufficient balance.")

elif choice == 3:
   print(f"Your balance is {balance}naira.")

elif choice == 4:
   num = int(input("Enter recipients number: "))
   amount = int(input("How much airtime will you like to transfer: "))

   if amount <= balance:
         print("Processing your request...")
         time.sleep(1)
         print("1")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print(f"You have successfully transferred {amount}naira to {num}.")
   else:
        print("Insufficient balance.")

#4. Car rental

print("\nCAR RENTAL")

print("1. Toyota.")
print("1. Honda.")
print("1. BMW.")
choice  = int(input("What car do you want to rent? "))
cost = 0
if choice == 1:
   rate = 50000
   print("Daily rate: 50,000NGN.")
   days = int(input("How many days would you like to rent this car? "))
   cost = rate * days
   print(f"The total cost for renting a Toyota for {days} day(s) is  {cost}NGN.")

elif choice == 2:
   rate = 30000
   print("Daily rate: 30,000NGN.")
   days = int(input("How many days would you like to rent this car? "))
   cost = rate * days
   print(f"The total cost for renting a Toyota for {days} day(s) is  {cost}NGN.")

elif choice == 3:
   rate = 100000
   print("Daily rate: 100,000NGN.")
   days = int(input("How many days would you like to rent this car? "))
   cost = rate * days
   print(f"The total cost for renting a Toyota for {days} day(s) is  {cost}NGN.")
else:
   print("Invalid option.")

# 5. Electricity billing

print("\nElectricity tariff billing.")
cost = 0
print("1. Residential.")
print("2. Commercial.")
print("3. Industry.")
category = int(input("What category are you? "))

if category == 1:
   rate_per_unit = 10
   unit = int(input("How manu unit have you used? "))
   cost = rate_per_unit * unit

   print(f"Your total electricity bill is {cost}NGN")
elif category == 2:
   rate_per_unit = 20
   unit = int(input("How manu unit have you used? "))
   cost = rate_per_unit * unit

   print(f"Your total electricity bill is {cost}NGN")
elif category == 3:
   rate_per_unit = 30
   unit = int(input("How manu unit have you used? "))
   cost = rate_per_unit * unit

   print(f"Your total electricity bill is {cost}NGN")
else:
   print("Invalid input.")


#6. Course registration system

print("\nCOURSE REGISTRATION SYSTEM.")

code = input("Enter your departmental code.(CSC, MTH, BIO, ENG.): ")
code = code.upper()
if code == "CSC":
   print("This is the computer science department.")
   print("Here are a list of your courses.")
   print("CIE 105\nCIE 106\nCSC 232 \nCSC 126")
elif code == "MTH":
   print("This is the mathematics department.")
   print("Here are a list of your courses.")
   print("MAT 210\nMAT 312\nGEC 134 \nGEC 135")
elif code == "BIO":
   print("This is the biology department.")
   print("Here are a list of your courses.")
   print("BIO 103\nATM 212\nPYI 111 \nBIO 121")
elif code == "ENG":
   print("This is the english department.")
   print("Here are a list of your courses.")
   print("WRI 101\nWRI 102\nENG 211 \nENG 312")
else:
   print("Invalid input.")

