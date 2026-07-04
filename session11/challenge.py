print("===PROGRAM TO CALCULATE THE SQUARE OF SUM and SUM OF SQUARES===")
a = float(input("Enter value for a: "))
b = float(input("Enter value for b: "))

square_of_sum = pow(a, 2) + pow(b, 2) + 2 * a * b
sum_of_squares = square_of_sum - (2 * a * b)
print(f"The square of the sum between {a} and {b} is {square_of_sum}")
print(f"The sum of the square between {a} and {b} is {sum_of_squares}")

