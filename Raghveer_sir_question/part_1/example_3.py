#Python program to calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter a number: "))
num = 0
for i in range(1, n + 1):
    num += i
print(num)

