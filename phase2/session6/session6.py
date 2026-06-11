"""
# Session: six
# Date: 21st may 2026 10am-12noon
# focus: List (if/else, for, while)
# Facilitator: Olatunbosun
 """
# #List [] 

# nameList = ["Ismail", "Gabriel", "Yakubu", "Caleb", "Fatima"]

# print(f"Echo List items out: {nameList}\n")
# print(f"Echo the data type of the variable:==> {type(nameList)}\n")

# # Remove from a list with pop(), remove(), clear
# nameList.pop()
# print(f"\nAfter pop method:==> {nameList}\n")
# # Pop() method with an index number
# nameList.pop(2)
# print(f"After pop with an index value:==> {nameList}")
# # Remove
# nameList.remove("Gabriel")
# print(f"\nAfter remove method:==> {nameList}\n")
# # Clear() method
# nameList.clear()
# print(f"\nprinting List aftr clear method:==> {nameList}\n")
# # Get the data type and count the list
# print(f"\nEcho the data type of the variable:==> {type(nameList)}\n")
# print(f"Number of the element in a List:==> {len(nameList)}\n")
# # Create empty List and items with append()
# print("\n\n------Create a List from an empty List------")
# fruitList =[]
# print(f"Empty List:==> {fruitList}\n")
# fruitList.append("Mango")
# print(f"Adding First Item:==> {fruitList}\n")
# fruitList.append("Cashew")
# print(f"Adding Second Item:==> {fruitList}\n")
# fruitList.append("254345754")
# print(f"Adding Third Item:==> {fruitList}\n")


# Extending List
# carStand1= ["Toyata"]
# carStand2 = ['BMW', 'Ford', 'Benz']
# carStand1.extend(carStand2)
# print(carStand1)
# countCars = len(carStand2)
# if countCars>=1:
#     print("count with if conditions:")
#     print(carStand1)
# else:
#     print("The two stand have no car list")    




# ## for, while, Do while
"""
# Session: six
# Date: 21st may 2026 1pm-3pmn
# focus: Dictionary {}
# Facilitator: Olatunbosun
# """

studentDict = {
    "name": "Marve", 
    "age": 12, 
    "phone":"+23480002993885", 
    "hobbies":["Tenis", "football", 'chess'],
    "score":{
        "math": 98,
        "english":25,
        "chemistry":38
    }
    }
clothSet = {"blouse", "trouser", "cap"}
# accessing dictionary values:
print(studentDict)

# Accessing Specific key values
print(studentDict["name"])
print(f"List of Keys: {studentDict.keys()}\n")
print(f"List of Values: {studentDict.values()}\n")

# Removing values
studentDict.pop("hobbies")
print(f"After removing hobbies: {studentDict}")
studentDict.popitem()
print(studentDict)
# Updating Values
studentDict["score"] = 98
print(f"Update value using predifined Key: {studentDict}")
studentDict.update({"score":30})
print(f"Updating value using update method: {studentDict}")
#Adding Values
studentDict.update({"parent":"Mangadu"})
print(f"Adding new key and value : {studentDict}")

#looping through Dictionaries, for and while
print(studentDict)
for x, y in studentDict.items():
    print(x,":", y)

print(f"\n --------while conditions---------")
n =0
studentKey = list(studentDict.keys())
studentValue = list(studentDict.values())
while n<len(studentKey):
    print(studentKey[n],":",studentValue[n])
    n +=1


# dynamic dictionary creation

nDict= {}

# while True:
#     key1 = str(input("Enter your Key: "))
#     value1 = str(input(f"Enter value for: {key1}"))
#     # nDict[key1] = value1
#     nDict.update({key1:value1})
#     print(nDict)


# Creating dictionary from a predefined length of key values

keyList = ["name", "age", "class"]

n = 1
while n <= len(keyList):
    valuel = str(input(f"Please enter values for {keyList[n-1]}: "))
    nDict.update({keyList[n-1]:valuel})
    n +=1
print(nDict)