# 22. Create a script to replace all occurrences of a given substring in a string with another substring.

# Function to replace all occurence in sa string
def replace_substring(original_str,old_string,new_string):
    # Using the replace() method to replace to old_string to new_string
    modified_str=original_str.replace(old_string,new_string)
    return modified_str

# Main Program
# Taking input from the user
original_str = input("Enter the original string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring: ")

# Call the function and display the result
modified_str = replace_substring(original_str, old_substring, new_substring)
print("Modified string:", modified_str)