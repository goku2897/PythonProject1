#Python program to calculate the sum of all the odd numbers within the given range.

n = int(input("Enter a number: "))
num = 0
for i in range(n+1):
    if i % 2 == 0:
       pass
    else:
        num += i
print(num)
