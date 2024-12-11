# 16. Write a function that calculates the factorial of a number provided by the user.

# Function to calculate the factorial of a number
def calculate_factorial(n):
    if n<0:
        return "Factorial is not a negative number."
    elif n==0 or n==1:
        return 1
    else:
        # Initialize the factorial is equal to 1
        factorial=1
        for i in range(1,n+1):
            factorial*=i
        return factorial
    
# Main program
# Input the user for a number
number = int(input("Enter a number to calculate its factorial: "))

# Calculating factorial using the function
result = calculate_factorial(number)

# Displaying the result
print("-----------------------------")
print(f"The factorial of {number} is: {result}")