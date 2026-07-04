

while True:
    name = input("Enter your name: ")
    if any(char.isdigit() for char in name):
        print("name cannot contain digits.")
        continue
    break

print(f"Hello, {name}")

