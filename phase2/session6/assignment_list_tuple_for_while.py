# 1. Average score.

scores = []
total = 0

num = int(input("Enter number of scores: "))

for x in range(num):
    score = int(input("Enter the score: "))
    scores.append(score)

for score in scores:
  total = total + score

average = total / num
print(f"The average score is {average: .2f}")

# 2. Savings
import time
savings = 0
week = 0
print("\n***Money saving system***")

while savings < 5000:
    savings = savings + 500
    week = week + 1
    print(f"You have saved 500NGN at the end of week {week} and your current balance is {savings}")
    time.sleep(2)

print(f"\nCongratulations. You have successfully saved {savings}NGN")

# 3. Multiplication table

print("\n***MULTIPLICATION TABLE***")

num = int(input("What multiplication table do you want: "))

for x in range(12):
    print(f"{num} * {x + 1} = {num * x + 1}")

#4.Password

Password = 123456
T = True

password = int(input("\nEnter password: "))
while password != Password:
    print("Incorrect password.")
    password = int(input("Enter password: "))

print("Access Granted!")

#5. SHOP

print("\n***SMALL SHOP***")
total = 0
prices = [500, 700, 1200]

for price in prices:
    total = total + price

print(f"\nTotal cost: {total}NGN.")

#6. ATM
print("\n***ATM***")

initial_balance = 50000

withdraw = 0

while initial_balance > 0:
    withdraw = int(input("Enter amount to withdraw: "))
    if withdraw <= initial_balance:
        initial_balance = initial_balance - withdraw
        print(f"You have successfully withdrawn {withdraw}NGN.")
        print(f"Remaining balance is {initial_balance}")

    elif withdraw > initial_balance:
        print(f"Withdrawal amount is greater than your balance, your remaining balance is {initial_balance}")

print("\nYou no longer have money in your account.")


#7. Login system

print("\nLogin system")

Username = "James Samson"
Password = 123456

username = input("Enter in your username: ")
password = int(input("Enter your password: "))

while username != "James Samson" or password != 123456:
    print("Incorrect login details.")

    username = input("Enter in your username: ")
    password = int(input("Enter your password: "))

print("\nLogin successful.")

#8.  Bus seat

seats = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Num =[]
for i in range(3):
    num = int(input("\nEnter seat number that has been booked: "))
    Num.append(num)

for i in range(3):
    seats.remove(Num[i])

print("The seats available are: ")
for seat in seats:
    print(f"seat {seat}")

#9. Temperature

temps = [39, 34, 38, 36, 38, 47, 42]
total = 0
for temp in temps:
    print(f"\nHighest value: {max(temps)} degrees celsius")
    print(f"Average value: {total / len(temps): .2f} degrees celsius")
    print(f"Lowest value: {min(temps)} degrees celsius")






