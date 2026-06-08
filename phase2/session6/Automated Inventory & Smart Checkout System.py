#The Automated Inventory & Smart Checkout System.

print("***WELCOME***")

option = 0
a = True

while a:
    print("---MAIN MENU---")
    print("1. View Inventory")
    print("2. Add/Update Inventory(Admin mode)")
    print("3. Smart Checkout(Customer mode)")
    print("4. Exit")
    try:
        option = int(input("Choose an option: "))
        if option < 1 or option > 4:
            print("\nOption must be between 1 and 4.")
            continue
    except ValueError:
        print("\nPlease enter a valid option.")
        continue
    match option:
        case 1:
            print()
        case 2:
            print()
        case 3:
            print()
        case 4:
            a = False

print("***BYE!!***")



