# 7. Given a tuple of integers, write a program to calculate the sum of all elements.

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

# Calculate the sum of all elements in the tuple
total_sum=sum(tuple1)

# Display the result
print("The sum of all elements in the tuple is:", total_sum)