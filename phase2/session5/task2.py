amount =float(input("Enter amount in USD: "))
if amount >= 1 and amount <= 500:
    Comission_Rate = 0.05
elif amount < 2000:
    Comission_Rate = 0.03
else:
    Comission_Rate = 0.015

Total_Comission = amount * Comission_Rate
print(f"The amount is ${amount:,.2f},\nYour comission is ${Total_Comission:,.2f}. Thankyou For Working With Us, Hope to see you again!")
