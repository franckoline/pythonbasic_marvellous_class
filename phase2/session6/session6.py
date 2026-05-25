"""
Session: six
Date: 21st May 2026 10:-12noon
focus: List (if/else, for, while, for)
Facilitator: Olatunbosun
"""

# # List []

# nameList = ["Ismail", "Gabriel", "Yakubu", "Japhet", "Caleb", "Fatima"]

# print(f"\nEcho list Items out:==> {nameList}\n")

# # Get the data type and count on the list
# print(f"\nEcho the data type of variable:==> {type(nameList)}\n")
# print(f"\nNumber of element in a list:==> {len(nameList)}\n")

# # Remove from a List with pop(), remove(), clear()
# nameList.pop()
# print(f"\nAfter pop method:==> {nameList}\n")
# # pop() method with an index number
# nameList.pop(2)
# print(f"After pop with an index value:==> {nameList}\n")
# # Remove()
# nameList.remove("Gabriel")
# print(f"\nAfter remove method:==> {nameList}\n")
# # Clear() method
# nameList.clear()
# print(f"\nPrinting list after Clear method:==> {nameList}\n")

# # print(f"Number of element in a list:==> {len(nameList)}\n")
# # Create Empty List and Add Items with append()
# print("\n\n\n-----Create a List from an empty List-----------")
# fruitList =[]
# print(f"Empty List:==> {fruitList}")

# fruitList.append("Mango")
# print(f"Adding First Item:==> {fruitList}")

# fruitList.append("Cashew")
# print(f"Adding Second Item:==> {fruitList}")

# fruitList.append(23495884)
# print(f"Adding Third Item:==> {fruitList}")
# # # Extending lists
# print("\n\n Extending List Items")
# carStand1 = ["Toyota"]
# carStand2 = ['BMW', 'Ford', 'Benz']
# carStand1.extend(carStand2)
# print(carStand1)
# countCars = len(carStand1)
# if countCars>=1:
#     print("Count with If Counditions:")
#     print(carStand1)
# else:
#     print("The two stand have no car list")


# ## for, while, Do while

# """
# Session: sixB
# Date: 21st May 2026 10:-12noon
# focus: Dictionary {}
# Facilitator: Olatunbosun
# """

# students = {
#     "student1":{},
#     "student2":{},
#     "student3":{}
    
# }
# studentDict = {
#     "name": "Olatunbosun", 
#     "age": 12, 
#     "phone":"+23480002993885", 
#     "hobbies":["Tenis", "football", 'chess'],
#     "score":{
#         "math": 98,
#         "english":25,
#         "chemistry":38
#     }
#     }
# clothSet = {"blouse", "trouser", "cap"}
# # accessing dictionary values:
# print(studentDict)

# # Accessing Specific key values
# print(studentDict["name"])
# print(f"List of Keys: {studentDict.keys()}\n")
# print(f"List of Values: {studentDict.values()}\n")

# # Removing values
# studentDict.pop("hobbies")
# print(f"After removing hobbies: {studentDict}")
# studentDict.popitem()
# print(studentDict)
# # Updating Values
# studentDict["score"] = 98
# print(f"Update value using predifined Key: {studentDict}")
# studentDict.update({"score":30})
# print(f"Updating value using update method: {studentDict}")
# #Adding Values
# studentDict.update({"parent":"Mangadu"})
# print(f"Adding new key and value : {studentDict}")

# #looping through Dictionaries, for and while
# print(studentDict)
# for x, y in studentDict.items():
#     print(x,":", y)

# print(f"\n --------while conditions---------")
# n =0
# studentKey = list(studentDict.keys())
# studentValue = list(studentDict.values())
# while n<len(studentKey):
#     print(studentKey[n],":",studentValue[n])
#     n +=1


# dynamic dictionary creation

# nDict= {}

# while True:
#     key1 = str(input("Enter your Key: "))
#     value1 = str(input(f"Enter value for: {key1}"))
#     # nDict[key1] = value1
#     nDict.update({key1:value1})
#     print(nDict)


# Creating dictionary from a predefined length of key values

# keyList = ["name", "age", "class"]

# n = 1
# while n <= len(keyList):
#     valuel = str(input(f"Please enter values for {keyList[n-1]}: "))
#     nDict.update({keyList[n-1]:valuel})
#     n +=1
# print(nDict)

# statem = str(input("Enter any value: "))
# while statem.lower() != "enter":
#     print("Please type 'ENTER' to begin to explore our service")
#     continue
# else:
#     print("Welcome to Session")

"""
Date:25th May 2026
Focus: try Except
"""

a = 34
b = 2
c = 43

try:
    d = a*b
    e = a-c
    f =d/e
    print(f"result :==> {f}")
except ZeroDivisionError:
    print(f"\n\n Numberator can not be divide by zero value \n")
except ValueError:
    print("")
except NameError:
    print("")
except IOError:
    print("")
else:
    print("You try block successfully")
finally:
    print("Task completed")