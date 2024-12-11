# 21. Write a program to count the number of words in a string.

# Function to count the number
def count_words(sentence):
    # Convert the string into lowercase
    words=sentence.lower()
    # Return the count of words
    return len(words)

# Main Program
# Taking input from the user
user_input = input("Enter a sentence: ")

# Call the function and display the result
print("------------------------------------------------")
word_count = count_words(user_input)
print(f"The number of words in the sentence is: {word_count}")