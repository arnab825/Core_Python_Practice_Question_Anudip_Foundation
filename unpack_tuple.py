# 10. Write a Python program to unpack a tuple into individual variables.

# create a blank list
list1=[]

# Input the elements of the list
num_elements = int(input("Enter the number of strings you want to input: "))

# Loop to accept user input and add it to the list
print("----------------------------------------------------")
print("Enter the elements:")


for i in range(num_elements):
    # Take input from the user
    element = input()  
    # Append the input to the list
    list1.append(element) 

# convert the list into tuple
tuple1=tuple(list1)

# Unpack the tuple into individual variables
# Assuming the tuple contains exactly as many elements as the number of variables
var1, var2, var3 = tuple1

# Display the individual variables
print("----------------------------------------------------")
print("Unpacked values:")
print("First variable:", var1)
print("Second variable:", var2)
print("Third variable:", var3)
