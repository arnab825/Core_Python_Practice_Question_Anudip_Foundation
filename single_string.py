# 9. Convert a tuple of strings into a single concatenated string using a loop.

# Create a blank list to store strings
list_of_strings = []

# Input the elements of the list
num_elements = int(input("Enter the number of strings you want to input: "))

# Loop to accept user 
print("Enter the name of the string:")

for i in range(num_elements):
    # Taking input from the user
    string1=input()
    # Insert the element of the list
    list_of_strings.append(string1)

# Convert the list of strings into a single concatenated string
concatenated_string = ""
for string in list_of_strings:
    # Concatenating each string
    concatenated_string += string  

# Display the concatenated string
print("Concatenated String:", concatenated_string)