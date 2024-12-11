# 23. Write a program to find the longest word in a sentence.

# Function to find the longest word
def find_longest_word(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize a variable to store the longest word
    longest_word = ""

    # Loop through the words to find the longest one
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word

# Main Program
# Taking input from the user
sentence = input("Enter a sentence: ")

# Call the function and display the result
longest_word = find_longest_word(sentence)
print("The longest word in the sentence is:", longest_word)
    
