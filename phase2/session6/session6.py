"""
Session: six
Date: 21st May 2026 10:-12noon
focus: List (if/else, for, while, for)
Facilitator: Olatunbosun
"""

# List []

nameList = ["Ismail", "Gabriel", "Yakubu", "Japhet", "Caleb", "Fatima"]

print(f"\nEcho list Items out:==> {nameList}\n")

# Get the data type and count on the list
print(f"\nEcho the data type of variable:==> {type(nameList)}\n")
print(f"\nNumber of element in a list:==> {len(nameList)}\n")

# Remove from a List with pop(), remove(), clear()
nameList.pop()
print(f"\nAfter pop method:==> {nameList}\n")
# pop() method with an index number
nameList.pop(2)
print(f"After pop with an index value:==> {nameList}\n")
# Remove()
nameList.remove("Gabriel")
print(f"\nAfter remove method:==> {nameList}\n")
# Clear() method
nameList.clear()
print(f"\nPrinting list after Clear method:==> {nameList}\n")

# print(f"Number of element in a list:==> {len(nameList)}\n")
# Create Empty List and Add Items with append()
print("\n\n\n-----Create a List from an empty List-----------")
fruitList =[]
print(f"Empty List:==> {fruitList}")

fruitList.append("Mango")
print(f"Adding First Item:==> {fruitList}")

fruitList.append("Cashew")
print(f"Adding Second Item:==> {fruitList}")

fruitList.append(23495884)
print(f"Adding Third Item:==> {fruitList}")
# # Extending lists
print("\n\n Extending List Items")
carStand1 = ["Toyota"]
carStand2 = ['BMW', 'Ford', 'Benz']
carStand1.extend(carStand2)
print(carStand1)
countCars = len(carStand1)
if countCars>=1:
    print("Count with If Counditions:")
    print(carStand1)
else:
    print("The two stand have no car list")