Total_kwh =float(input("What is your Total kWh consumption?: "))

if Total_kwh <= 50:
    bill = Total_kwh * 30
elif Total_kwh <= 200:
    bill = (50 * 30) + ((Total_kwh - 50) * 50)
else:
    bill = (50 * 30) + (150 * 50) + ((Total_kwh - 200) * 85)

if bill > 20000:
    bill += 1000
    print("Maintenance Levy of ₦1,000 applied.")
print(f"Total amount due: ₦{bill:.3f}")
