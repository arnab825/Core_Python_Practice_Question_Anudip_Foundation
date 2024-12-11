# 3. Write a program to remove duplicate items from a list while maintaining order.

# Function to remove duplicates while maintaining order
def remove_duplicates(input_list):
    seen = set()  # Set to store the already encountered elements
    result = []  # List to store the final result without duplicates

    # Loop through the input list
    for item in input_list:
        # If the item is not in the seen set, add it to the result list
        if item not in seen:
            result.append(item)
            seen.add(item)  # Add the item to the seen set

    return result

# Main Program
# Taking input from the user
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
# Removing duplicates while maintaining order
result = remove_duplicates(numbers)

# Displaying the result
print("List without duplicates:", result)
