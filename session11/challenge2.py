print("===PROGRAM TO CALCULATE THE DIFFERENCE BETWEEN THE SQUARE OF SUM and SUM OF SQUARES===")
n = int(input("Enter the number of terms: "))
sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
square_of_sum = pow(((n * (n + 1)) / 2)  , 2)

difference = square_of_sum - sum_of_squares
print(square_of_sum)
print(sum_of_squares)
print(f"The difference between the square of sum and the sum of squares is: {difference}")




