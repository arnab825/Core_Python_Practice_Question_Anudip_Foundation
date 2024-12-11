# 8. Write a Python script to check if an element exists in a tuple.

# create a blank list
list1=[]

# Input the elements of the list
num_elements = int(input("Enter the number of elements you want to input: "))

# Loop to accept user input and append to the list
print("----------------------------------------------------")
print("Enter the elements:")

for i in range(num_elements):
    # Input each number
    num=int(input())
    # Insert the element of the list 
    list1.append(num)

print("List of the Elements:",list1)


# Convert a list into tuple
tuple1=tuple(list1)
print("Coverting the List to Tuple:",tuple1)

# Ask the user for an element to check
element = int(input("Enter an element to check if it exists in the tuple: "))

# Check if the element exists in the tuple
if element in tuple1:
    print(element," exists in the tuple.")
else:
    print(element," does not exist in the tuple.")

