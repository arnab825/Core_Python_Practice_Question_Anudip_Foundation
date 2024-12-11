# 6. Write a program to find the index of an element in a tuple.

print("Enter the elements of the list (separated by spaces):")
list_elements = list(map(int, input().split()))  # Convert input to a list of integers

# Convert the list to a tuple
tuple_elements = tuple(list_elements)

# Input: The element to find
element = int(input("Enter the element to find its index: "))

# Finding the index of the element in the tuple
if element in tuple_elements:
    index = tuple_elements.index(element)
    print(f"The index of {element} in the tuple is: {index}")
else:
    print(f"{element} is not found in the tuple.")