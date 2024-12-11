# 28. Write a Python program to calculate the sum of all odd numbers up to a given number 'n'.
# Function to calculate the odd number up to n
def sum_of_odd_numbers(n):
    # Initialize the sum of odd number is 0
    sum_odd=0
    # Looping through all number from 1 to n
    for i in range(1,n+1,2):
        # Add the odd number to the sum
        sum_odd+=i
    return sum_odd

# Main Program
# Take input fom the user
print("----------------------------------------")
num=int(input("Enter the number :"))

# Call the function and calculate the sum of odd number
result=sum_of_odd_numbers(num)

# Display the result
print("----------------------------------------")
print(f"The sum of all odd numbers up to {num} is: {result}")
