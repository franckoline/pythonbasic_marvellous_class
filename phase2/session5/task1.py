Years_in_Business =int(input("How old are you in the Business?: "))
Monthly_Revenue =float(input("What is your monthly revenue?:"))

if Years_in_Business > 3 or Monthly_Revenue < 200000:
    print("Eligible for Grant")
else:
    print("Not Eligible")    
  

