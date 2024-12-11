# 20. Write a recursive function to calculate the nth Fibonacci number.


# Recursive function to calculate the nth Fibonacci number
def fibonacci_number(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0  # The 1st Fibonacci number is 0
    elif n == 2:
        return 1  # The 2nd Fibonacci number is 1
    else:
        return fibonacci_number(n - 1) + fibonacci_number(n - 2)

# Main program
# Taking input from the user
n = int(input("Enter the position (n) of the Fibonacci number you want: "))

# Call the function and display the result
result = fibonacci_number(n)
print(f"The {n}th Fibonacci number is: {result}")
