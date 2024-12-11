# 4. Create a program that finds the intersection of two lists.

# Main Program
# Taking input for the first list
list1 = list(map(int(input("Enter elements for the first list (separated by spaces):").split())))  # Convert input string to list of integers

# Taking input for the second list

list2 = list(map(int( input("Enter elements for the second list (separated by spaces):").split())))  # Convert input string to list of integers

# Finding the intersection of the two lists
intersection = list(set(list1) & set(list2))

# Displaying the result
print("Intersection of the two lists:", intersection)
