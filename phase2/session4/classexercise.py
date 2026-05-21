# num1
#bjusiness_name =str(input("What is the Business Name?: ")) 
#owner_name = str(input("What is the Owners Name?: "))
#owner_age = int(input("What is the Owners Age?: "))
#business_type = str(input("Type of Business?: "))
#country = str(input("Country: "))
#monthly_revenue = float(input("What is your Monthly Revenue?: "))
#number_of_employees = int(input("Number of Employees?: "))
#years_in_operation = str(input("How many years have you been in Operation?: "))
#is_the_business_registered = str(input("Is the Business Registered (yes/no)?: "))
#business_tax_id = str(input("Does the Business have a tax ID (yes/no)?: "))
 
'''if owner_age >= 18:
      
    print(f"hey {owner_name}, your are up to the required age! You are approved to go ahead! ")
else:
    print(f"hey {owner_name}, we're sorry to inform you that {owner_age} did not meet the required age.")
'''
#-----------------------------------------------------------------------------------
   #num2
'''monthly_revenue =float(input("What is your Monthly Revenue?: "))
time_in_business =int(input("How many years have you been in the Business?: "))
business_registered =str(input("Is the Business Registered?: "))
business_tax_id =str(input("Does the Business have a Tax ID?: "))

if monthly_revenue < 50000 and time_in_business >= 2:
    print("you are eligible")
    if business_registered == 'yes' and business_tax_id == 'yes':
        print("You are Eligible!")
    else:
        print("you are not Eligible")
else:
    print("you are not eligible")'''   

#--------------------------------------------------------------------------------



   #num3
'''revenue = float(input("What is your Revenue?: "))
employees = int(input("How many employees do you have?: "))
registered = str(input("Is your business Registered?(yes/no): "))

if revenue > 1000000 or employees < 2 or registered == 'no':
    print("Fraudulent activity detected")
else:
    print("Good to go!")'''  

#-----------------------------------------------------------------------


   #num4
'''annual_revenue = int(input("What is your Annual Revenue?: "))

if annual_revenue <= 200000:
    print("This ia a Startup Business")
elif annual_revenue  <= 500000:
    print("This is a Small Business") 
elif annual_revenue <= 1000000:
    print("This is Meduim Enterprise")
else:
    print("This is a Large Coporation")'''

#-----------------------------------------------------------------


    #num5
'''annul_revenue = int(input("What is your Annual Revenue?: "))
bussiness_years = int(input("How old is the Business(years)?: "))

if annul_revenue > 100000 or bussiness_years > 10:
    print("You are Qualified")
else:
    print("dear user i am sorry to inform you that your information does not meet our specifications.")'''       

#------------------------------------------------------------------------
    

#num6
'''years_in_operations = int(input("How many years have you been in operation?: "))
annual_revenue = int(input("What is your annual Revenue?: "))
num_of_employees = int(input("How many employees do you have?: "))
country  = str(input("What country is the bussiness in?: "))

if years_in_operations > 5 and annual_revenue > 200000 and num_of_employees > 20 and country != 'Ghana, SouthAfrica':
    print("Congratulations! You are qualified for international expansion")
else:
    print("we are sorry to inform you that you do not meet our specific requirements.")'''    

#------------------------------------------------------------------------

#num7
'''annual_revenue = int(input("What is your Annual Revenue?: "))
if annual_revenue < 10000:
    print("Your tax rate is 5%")
elif annual_revenue < 50000:
    print("Your tax rate is 10%")    
elif annual_revenue < 200000:
    print("Your tax rate is 18%")
else:      
    print("Your tax rate is 25%")'''

#----------------------------------------------------------------


#num8
'''registered = str(input("Are you Registered(yes/no)?: "))
tax_id = str(input("Do you have an existing Tax ID(yes/no)?: "))
annual_revenue = int(input("What is your Annual Revenue?: "))
employees = int(input("How many employees do you have?: "))
operation_years = int(input("How many years have you been in operation?: "))'''

#------------------------------------------------------------------
#num9
name = str(input("What is your Full Name?: "))
dob = str(input("What is your date of birth?: "))
state_of_origin = str(input("what is your state of Origin?: "))
print()
print()
print("------DRIVERS LICENCE-----")
print(f"NAME--[{name}]\nD.O.B--[{dob}]\nSTATE OF ORIGIN--[{state_of_origin}]")


    
