"""
Session: Ten
Date: 8th June 2026 9:30am
focus: Churn Probability
Facilitator: Olatunbosun
"""

customer_data = [
    {"id": 101, "support_tickets": 1, "churned": 0},
    {"id": 102, "support_tickets": 5, "churned": 1},
    {"id": 103, "support_tickets": 3, "churned": 1},
    {"id": 104, "support_tickets": 0, "churned": 0},
    {"id": 105, "support_tickets": 4, "churned": 1},
    {"id": 106, "support_tickets": 2, "churned": 0},
    {"id": 107, "support_tickets": 1, "churned": 0},
    {"id": 108, "support_tickets": 6, "churned": 1},
    {"id": 109, "support_tickets": 0, "churned": 0},
    {"id": 110, "support_tickets": 3, "churned": 0}
]

total_customers = len(customer_data)


churn_events = [customer["churned"] for customer in customer_data]
print("printing customer\n")
print(churn_events)
print("printing customer\n")
total_churned = sum(churn_events)

p_churn = total_churned / total_customers

print("--- Business-Wide Metrics ---")
print(f"Total Customers Monitored: {total_customers}")
print(f"Total Customers Lost (Churned): {total_churned}")
print(f"Baseline Probability of Churn: {p_churn:.2f} ({p_churn * 100:.1f}%)")


print("\n--- Predictive Risk Analysis ---")

"""
Conditional Population
"""
# Filter space for high-ticket customers
high_ticket_customers = [c for c in customer_data if c["support_tickets"] > 2]
print("printing customer")
print(high_ticket_customers)
print("printing customer\n")
total_high_ticket = len(high_ticket_customers)

# Count how many of these high-ticket customers actually churned
high_ticket_churned = sum([c["churned"] for c in high_ticket_customers])

# Calculate Conditional Probability: P(Churn | Tickets > 2)
if total_high_ticket > 0:
    p_churn_given_high_tickets = high_ticket_churned / total_high_ticket
    print(f"Customers with > 2 Support Tickets: {total_high_ticket}")
    print(f"Churned within this specific group: {high_ticket_churned}")
    print(f"Probability of Churn if Tickets > 2: {p_churn_given_high_tickets:.2f} ({p_churn_given_high_tickets * 100:.1f}%)")
else:
    print("No customers matched the criteria.")


print("\n\n New Dataset \n\n")
print(customer_data)
print('\n\n New data')
print(high_ticket_customers)