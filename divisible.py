# 30. Write a script to find all numbers between 100 and 200 that are divisible by 5 but not by 3.

print("------------------------------------------")
print("All numbers between 100 and 200 that are divisible by 5 but not by 3 are")
# Loop through numbers from 100 to 200
for num in range(100,201):
    # Check if the number is divisible by 5 but not by 3
    if num % 5 == 0 and num % 3 != 0:
        print(num)
