name_of_product = str(input("Enter the name of your product: "))
original_price = float(input("Original price: "))
discount_percentage = float(input("Discount percentage: "))
discount_amount = (discount_percentage / 100) * original_price
final_price = original_price - discount_amount
print(f"Final price: {final_price}")
