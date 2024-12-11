# 2. Given a list of numbers, write a program to find all the even numbers and store them in a new list.

# Function to find the even numbers in a list
def even_number(n):
    # Empty list to store even numbers
    even_numbers = []

    # Loop through the list
    for num in n:
        if num % 2 == 0:
            # Append the even number to the list
            even_numbers.append(num)
    return even_numbers

# Main Program

# Input the number of elements
num_elements = int(input("Enter the number of elements you want to input:"))  

# Creating an empty list to store numbers
numbers = []

# Loop to accept the user's input and append to the list
print("-----------------------------------------------------")
print("Enter the numbers:")
for i in range(num_elements):
    num = int(input())  # Input each number
    numbers.append(num)  # Append to the numbers list



print("------------------------------------")
print(numbers)
# Finding the even numbers using the function
result = even_number(numbers)

# Displaying the result
print("Even numbers in the list:", result)
