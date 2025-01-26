#Python program to print all the even numbers within the given range.

n = int(input("Enter a number: "))

for i in range(n+1):
    if i % 2 == 0:
        print(i)
