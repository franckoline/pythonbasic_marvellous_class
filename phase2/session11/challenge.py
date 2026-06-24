import random
# Task 1: Calculate the Baseline Probability of Churn - Using the standard probability formula, determine the overall risk across the entire business.
# Task 2: Isolate the "High Support" Risk Group - Filter the sample space to find customers who are showing signs of frustration.
# Task 3: Calculate the Conditional Probability of Churn — $P(\text{Churn} \mid \text{Tickets} > 3)#
# Task 4: Print out a clear summary to the console displaying:
#     --The baseline churn rate as a percentage.
#     --The conditional churn rate for frustrated users as a percentage.
#     --A written conclusion answering: Should the customer success team prioritize users with more than 3 tickets?

#Task 1

customer_data = []
customer_dict = {}


for i in range(10):
    customer_dict["id"] = random.randint(101, 111)
    customer_data.append(customer_dict)

print(customer_data)

