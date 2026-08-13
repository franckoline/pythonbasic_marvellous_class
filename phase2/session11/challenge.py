import random

# Setting a fixed seed so every student gets the same results
random.seed(42)

total_customers = 1000
customer_database = []

# Generate data logs for 1,000 customers and store it in memory
for customer_id in range(101, 101 + total_customers):
    # Support tickets filed by the customer this month (0 to 8)
    tickets = random.randint(0, 8)
    
    # Conditional logic determines churn likelihood for the simulation
    if tickets > 3:
        # High tickets = 70% chance of churning
        churned = 1 if random.random() < 0.70 else 0
    else:
        # Low tickets = 15% chance of churning
        churned = 1 if random.random() < 0.15 else 0
        
    customer_database.append({
        "id": customer_id,
        "support_tickets": tickets,
        "churned": churned
    })

print(f"--- Database Initialized ---")
print(f"Successfully loaded {len(customer_database)} customer monitoring profiles.")

"""
Tasks
Task 1: Calculate the Baseline Probability of Churn - Using the standard probability formula, determine the overall risk across the entire business.
Task 2: Isolate the "High Support" Risk Group - Filter the sample space to find customers who are showing signs of frustration.
Task 3: Calculate the Conditional Probability of Churn — $P(\text{Churn} \mid \text{Tickets} > 3)#
Task 4: Print out a clear summary to the console displaying:
    --The baseline churn rate as a percentage.
    --The conditional churn rate for frustrated users as a percentage.
    --A written conclusion answering: Should the customer success team prioritize users with more than 3 tickets?
"""