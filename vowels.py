# 19. Create a function that takes a string and returns the count of vowels in it.

# function to count number of vowels
def count_vowels(sentence):
    # initializing the vowel count as 0
    vowels=0
    # Converting the sentence into lowercase
    str1=sentence.lower()
    # Loop through each character through the string
    for i in str1:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            vowels+=1
    return vowels

# Main program
# Taking input from the user
user_input = input("Enter a string: ")
# Call the function and display the result
print("-----------------------------------------")
vowel_count = count_vowels(user_input)
print(f"The number of vowels in the string is: {vowel_count}")