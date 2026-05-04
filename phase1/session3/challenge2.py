brand_name = input("brand name: ")
monthly_income = float(input("total monthly income: "))
marketing_spend = float(input(" marketing spend: "))

percentage = (marketing_spend / monthly_income) * 100
balance = monthly_income - marketing_spend

print(f"Brand {brand_name} has the ${balance:.2f} remaining after a {percentage:.2f}% marketing investment.")
