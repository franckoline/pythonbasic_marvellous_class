inventory = {
    "PROD001": ("Laptop", 999.99, 10),
    "PROD002": ("Wireless Mouse", 25.50, 50),
    "PROD003": ("Headphones", 149.00, 15),
    "PROD004": ("Coffee Mug", 12.00, 5)
}

discount_items = {"PROD001", "PROD003"}


def generate_receipt(cart_data, discount_set, inventory_ref):
    receipt_lines = []
    grand_total = 0.0


    receipt_lines.append("=" * 45)
    receipt_lines.append("               OFFICIAL RECEIPT              ")
    receipt_lines.append("=" * 45)
    receipt_lines.append(f"{'ITEM'.ljust(18)}{'QTY'.ljust(6)}{'PRICE'.ljust(10)}{'TOTAL'.rjust(11)}")
    receipt_lines.append("-" * 45)

    for prod_id, qty in cart_data.items():
        item_name, original_price, amount = inventory_ref[prod_id]


        price_per_unit = original_price
        is_discounted = prod_id in discount_set
        if is_discounted:
            price_per_unit = original_price * 0.9

        item_total = price_per_unit * qty
        grand_total += item_total


        display_name = item_name
        if is_discounted:
            display_name += " (10% OFF)"

        receipt_lines.append(f"{display_name.ljust(18)}{str(qty).ljust(6)}${price_per_unit:.2f}".ljust(
            34) + f"${item_total:.2f}".rjust(11))

    receipt_lines.append("-" * 45)
    receipt_lines.append(f"{'GRAND TOTAL:'.ljust(34)}${grand_total:.2f}".rjust(45))
    receipt_lines.append("=" * 45)
    receipt_lines.append("          THANK YOU FOR YOUR PATRONAGE!      ")
    receipt_lines.append("=" * 45)


    print("\n")
    for info in receipt_lines:
        print(info)
    print("\n")


print("*** WELCOME TO THE SMART RETAIL SYSTEM ***")

a = True
while a:
    print("\n" + "--- MAIN MENU ---")
    print("1. View Inventory")
    print("2. Add/Update Inventory (Admin Mode)")
    print("3. Smart Checkout (Customer Mode)")
    print("4. Exit")

    try:
        option = int(input("Choose an option (1-4): "))
        if option < 1 or option > 4:
            print("\n[Error] Option must be between 1 and 4.")
            continue
    except ValueError:
        print("\n[Error] Please enter a valid number.")
        continue

    match option:

        case 1:
            print("\n" + "=== CURRENT INVENTORY ===")
            print("-" * 55)
            for prod_id, details in inventory.items():
                name, price, stock = details
                print(f"{prod_id.upper().ljust(10)}{name.ljust(20)}${price:.2f}".ljust(42) + f"{stock}".rjust(13))
            print("-" * 55)

        case 2:
            print("\n--- ADMIN MODE: ADD/UPDATE STOCK ---")
            prod_id = input("Enter Product ID (e.g., PROD005): ").strip().upper()
            name = input("Enter Product Name: ").strip()


            while True:
                try:
                    price = float(input("Enter Product Price ($): "))
                    if price < 0:
                        print("[Error] Price cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("[Error] Invalid input. Price must be a decimal number.")

            while True:
                try:
                    quantity = int(input("Enter Stock Quantity: "))
                    if quantity < 0:
                        print("[Error] Quantity cannot be negative.")
                        continue
                    break
                except ValueError:
                    print("[Error] Invalid input. Quantity must be a whole integer.")


            inventory[prod_id] = (name, price, quantity)
            print(f"\n[Success] {name} updated inside inventory database.")

        case 3:
            print("\n--- CUSTOMER MODE: SMART CHECKOUT ---")
            print("Type 'done' at any time to finalize your purchase.\n")

            customer_cart = {}

            while True:
                user_choice = input("Enter Product ID to buy (or 'done'): ").strip().upper()

                if user_choice == 'DONE':
                    break

                if user_choice not in inventory:
                    print("[Error] Product ID not found in database. Try again.")
                    continue

                item_name, price, current_stock = inventory[user_choice]

                if current_stock == 0:
                    print(f"[Error] Sorry, {item_name} is completely out of stock.")
                    continue

                try:
                    buy_qty = int(input(f"How many units of {item_name} would you like? "))
                    if buy_qty <= 0:
                        print("[Error] Quantity must be greater than 0.")
                        continue
                except ValueError:
                    print("[Error] Invalid input. Please enter a whole integer.")
                    continue

                if buy_qty > current_stock:
                    print(f"[Error] Cannot fulfill request. Only {current_stock} units left in stock.")
                    continue

                updated_stock = current_stock - buy_qty
                inventory[user_choice] = (item_name, price, updated_stock)

                if user_choice in customer_cart:
                    customer_cart[user_choice] += buy_qty
                else:
                    customer_cart[user_choice] = buy_qty

                print(f"[Added] {buy_qty}x {item_name} added to your checkout session.")

            if customer_cart:
                generate_receipt(customer_cart, discount_items, inventory)
            else:
                print("\n[Info] Checkout cancelled. Your cart was empty.")

        case 4:
            a = False

print("\n*** BYE!! ***")