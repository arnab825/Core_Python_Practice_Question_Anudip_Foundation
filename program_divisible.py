# 26. Write a program to print all numbers from 1 to 100 that are divisible by 7.

print("---------------------------------")
print("All Numbers from 1 to 100 that are divisible by 7 are:")
for num in range(1,101):
    if num%7==0:
        print(num)
