color = input("Favorite color: ").strip()
noun = input("A noun that represents your brand: ").strip()
birth_year = input("Birth year: ").strip()

handle = f"@{color}{noun}{birth_year}"
print(f"Your new brand handle is: {handle}")