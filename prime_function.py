# 17. Create a function that accepts a list of numbers and returns a new list with only the prime numbers.

# Function to check if it is prime
def is_prime(n):
    # Handle special cases for 0 and 1
    if n == 0 or n == 1:
        return False
    # Check for factors
    elif n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False  # Not a prime number
        return True  # Prime number
    else:
        return False  # For invalid input like negative numbers
    
# Function to filter prime numbers
def filter_primes(numbers):
    prime_list = []  # Blank list to store prime numbers
    for num in numbers:
        if is_prime(num):
            prime_list.append(num)  # Add prime numbers to the list
    return prime_list

# Main program
# Input the user has the list of a number
print("Enter the numbers separated by spaces:")
numbers = list(map(int, input().split()))


# Filtering prime numbers
prime_numbers = filter_primes(numbers)

# Displaying the result
print("-----------------------------")
print("Original List:", numbers)
print("List of Prime Numbers:", prime_numbers)