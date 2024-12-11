# 27. Create a program to print a pyramid pattern of asterisks (*) with n levels.

# function to print pyramid pattern

def is_pyramid_pattern(n):
    
    for i in range(1,n+1):
        # Print spaces to align the star in the centre
        print(" "*(n-i),end="")

        # Print star to the current level
        print("*" * (2 * i - 1))

# Main program
# Take 'n' is the number of level from the input user
print("----------------------------------------")
n=int(input("Enter the number of levels for the pyramid: "))

# Call the function 
is_pyramid_pattern(n)