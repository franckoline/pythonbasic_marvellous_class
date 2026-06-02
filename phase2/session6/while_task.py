#1. Number guessing game.
import random

print("Number guessing game.")
number = random.randint(1 , 20)

guess = 0
while guess != number:
   guess = int(input("Guess a number from 1 to 20: "))

   if guess > number:
       print("Too high.")
   elif guess < number:
       print("Too low.")



print(f"You got the number {number} correct.")


#2. Password feedback Validator.
print("\nPassword validator.")

password = input("Enter a password: ")



while password.isalpha() or len(password) < 8 or password.islower():
    if password.isalpha():
        print("Password must contain at least one digit.")

    if len(password) < 8:
        print("Password must contain at least 8 digits.")

    if password.lower():
        print("Password must contain at least one uppercase letter.")

    password = input("Enter a password: ")

print("You have successfully entered a password.")

#3. ATM simulation

print("\n***WELCOME TO THE ATM.***")

option = 10
balance = 1000000

while option == 10:
    print("\n1. Withdraw.")
    print("2. Deposit.")
    print("3. Check bank balance..")
    print("4. Exit.")
    choice = int(input("Pick an option: "))

    if choice == 1:
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
        else:
            new_balance = balance - amount
            print(f"You have successfully withdrawn ${amount} and your balance is now ${new_balance}.")
            print("Thank you for using our service.")
    if choice == 2:
        amount = int(input("Enter amount to deposit: "))
        new_balance = balance + amount
        print(f"You have successfully deposited ${amount} and your balance is now ${new_balance}. ")
        print("Thank you for using our service.")
    if choice == 3:
        print(f"Your account balance is ${balance}.")
        print("Thank you for using our service.")
    if choice == 4:
        option = 1
        print("Thank you for using our services. BYE!!!")