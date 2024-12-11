# 18. Write a Python function to check if a given string is a palindrome.

# Function to check if a string is a palindrome
def is_palidrome(name):
    # Convert the name into the lowercase
    name1=name.lower()
    # Check the name is equal to reverse
    return name1==name1[::-1]

# Main program
# Taking input from the user
user_input = input("Enter a string: ")

# Call the function and display the result
if is_palidrome(user_input):
    print(user_input,"is a palindrome.")
else:
    print(user_input,"is not a palindrome.")