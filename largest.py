# 1. Write a Python program to find the largest number in a list without using the max() function.

# function to find the largest number
def find_largest(n):
    # initialize the largest number
    largest=n[0]

  # Iterating the list to compare the each element
    for num in n:
        if num>largest:
            largest=num
    return largest


# Main Program
# Taking input from the user
num_elements = int(input("Enter the number of elements you want to input:"))

# Creating an empty list
numbers = []


# Looping to accept the user's input and append to the list
print("-----------------------------------------------------")
print("Enter the numbers:")
for i in range(num_elements):
    num=int(input())
    # add the element of the list
    numbers.append(num)

print("------------------------------------")
print(numbers)
# Finding the largest number and calling the function
result= find_largest(numbers)

# Displaying the result
print("The largest number in the list is:", result)

