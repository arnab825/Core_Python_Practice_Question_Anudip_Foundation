# 12. Create a program to find the key with the maximum value in a dictionary.

# Create a blank dictionary
data_dict = {}

# Input the user has to input-user
num_entries = int(input("Enter the number of key-value pairs you want to input: "))

print("Enter the key-value pairs (key followed by value):")
for i in range(num_entries):
    key = input("Key: ")  # Input key
    value = int(input("Value: "))  # Input value (assuming values are integers)
    data_dict[key] = value  # Add the key-value pair to the dictionary

# Find the key with the maximum value
max_key = max(data_dict, key=data_dict.get)

# Display the result
print("-----------------------------")
print("Dictionary:", data_dict)
print("Key with the maximum value:", max_key)
print("Maximum value:", data_dict[max_key])