#1. Site Safety Checklist Validator

def check_safety_compliance(checklist):

    for items in checklist.values():
        if not items:
            return False

    return True


Checklist = {
        "helmet": True,
        "gloves": True,
        "fire-extinguisher": True,
        "sand_bucket": True,
        "mask": True}



print(check_safety_compliance(Checklist))

# 2. Equipment Usage Tracker


def track_equipment_usage(logs):
    total_hours = {}

    for name , time in logs:
        if name in total_hours:
            total_hours[name] += time
        else:
            total_hours[name] = time


    return total_hours


machinery_logs = [
    ("Excavator", 5.5),
    ("Forklift", 2.0),
    ("Excavator", 3.0),
    ("Crane", 4.5),
    ("Forklift", 1.5)
]
print(track_equipment_usage(machinery_logs))

#3. Invoice Generator

def generate_invoice(client_name, items):
    invoice = []
    total_amount = 0

    invoice.append(f"Invoice for {client_name}")

    for description, unit_price, quantity in items:
        total = unit_price * quantity
        total_amount += total

        invoice.append(
            f"{description}-----"
            f"Unit Price: ${unit_price}-----"
            f"Quantity: {quantity}----"
            f"Total Price: ${total}"
        )


    return invoice

Items = [("Monitor", 5000, 4),
         ("Mouse", 12, 2),
         ("Keyboard", 34, 3),
         ("Stylus", 10, 1)
         ]

generate_invoice("Prince", Items)
print(generate_invoice("Prince", Items))

