# TASK1

# Calculate the Baseline Probability of Churn
customers = [
    {"name": "mary", "ticket": 6, "churn": 1},
    {"name": "john", "ticket": 7, "churn": 1},
    {"name": "marve", "ticket": 2, "churn": 0},
    {"name": "victor", "ticket": 0, "churn": 0},
    {"name": "samuel", "ticket": 1, "churn": 0},
    {"name": "grace", "ticket": 4, "churn": 0}
]    

total_customers = len(customers)

# Churn = total churned/total customers * 100
total_churned = 0
for i in customers:
    if i ["churn"] == 1:
        total_churned += 1

    
baseline_probability = total_churned/total_customers

print(baseline_probability*100)



#TASK2

# Isolate the high support risk group

risk_group = []

for i in customers:
    if i["ticket"] > 3:
        risk_group.append(i)

print(risk_group)



#TASK3

#Calculate the Conditional Probability of Churn

risk_group_total = len(risk_group)

risk_group_churn = 0
for i in risk_group:
   if i["churn"] == 1:
    risk_group_churn += 1

risk_group_total = risk_group_churn/risk_group_total

print(risk_group_total)


#TASK4

#Print out a clear summary to the console displaying

print("----- Customer Churn Analysis -----")

print(f"Baseline churn rate: {baseline_probability * 100}%")

print(f"High support churn rate: {risk_group_total* 100}%")


if risk_group_total > baseline_probability:
    print("Prioritize users with more than 3 tickets because they have a higher risk of churn.")
else:
    print("Users with more than 3 tickets do not show a higher churn risk.")