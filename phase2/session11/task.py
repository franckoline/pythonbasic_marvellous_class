# Task 1: Calculate the Baseline Probability of Churn - Using the standard probability formula, determine the overall risk across the entire business.
# Task 2: Isolate the "High Support" Risk Group - Filter the sample space to find customers who are showing signs of frustration.
# Task 3: Calculate the Conditional Probability of Churn — $P(\text{Churn} \mid \text{Tickets} > 3)#
# Task 4: Print out a clear summary to the console displaying:
#     --The baseline churn rate as a percentage.
#     --The conditional churn rate for frustrated users as a percentage.
#     --A written conclusion answering: Should the customer success team prioritize users with more than 3 tickets?
import random
#Task 1

# Pick unique names for n number of customers.
n = 10
name_list = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver",
    "Ava", "Elijah", "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin", "Isabella", "Lucas",
    "Mia", "Henry", "Evelyn", "Alexander", "Harper"
]
customer_data = []
names = random.sample(name_list, n)
for name in names:
    customer_data.append({"name" : name})

#Generate random number of complaints for each customer.
complains = random.sample(range(0, 10), n)
for index, customer in enumerate(customer_data):
    customer.update({"number of complains" : complains[index]})

#Generate random churn for each customer
for customer in customer_data:
    if customer["number of complains"] == 0:
        customer["churned"] = 0
    elif customer["number of complains"] > 5:
        customer["churned"] = 1 if random.random() < 0.80 else 0
    else:
        customer["churned"] = 1 if random.random() < 0.20 else 0

# Calculate baseline probability if churn
num_of_churn = 0
for customer in customer_data:
    if customer["churned"] == 1:
        num_of_churn += 1
prob_churn = num_of_churn / len(customer_data)

#Task 2 - Isolating the "High support" risk group
high_support = []
for customer in customer_data:
    if customer["number of complains"] > 5:
        high_support.append(customer)

#Task 3

#Calculate total number if total high support churned
total_high_support_churned = 0
for customer in high_support:
    if customer["churned"] == 1:
        total_high_support_churned += 1

#Calculate the conditional probability of churned given complains is greater than 5

if len(high_support) > 0:
    prob_churn_given_high_complains = total_high_support_churned / len(high_support)
else:
    print("There are no customers with more than 5 complains.")
    prob_churn_given_high_complains = 0.0

#Task 4 - Printing result
print("\n===BUSINESS RISK ANALYSIS===")
print(f"Baseline Probability of Churn: {prob_churn * 100:.1f}%")
print(f"Conditional churn rate of frustrated customers: {prob_churn_given_high_complains * 100:.1f}%")
if prob_churn_given_high_complains > 0.60:
    print("The customer success team should prioritize solving the issue of customers with more than 5 complains,")
    print("Because,the conditional churn rate is significantly higher than the base churn rate.")
else:
    print("The customer success team do not need to prioritize solving the issue of customers with more than 5 complains,")
    print("Because,the conditional churn rate is lower than the base churn rate.")








