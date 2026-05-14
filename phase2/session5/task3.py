Total_kwh =float(input("What is your Total kWh consumption?: "))

if Total_kwh <= 50:
    bill = Total_kwh * 30
elif Total_kwh <= 200:
    bill = Total_kwh * 50
else:
    bill = Total_kwh * 85

if bill > 20000:
    bill += 1000
    print("Maintenance Levy of ₦1,000 applied.")
print(f"Total amount due: ₦{bill:.3f}")
