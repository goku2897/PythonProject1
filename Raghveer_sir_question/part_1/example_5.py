#Python program to print a multiplication table of a given number

num = int(input("Enter a number: "))

for i in range(num+1):
    print("{num} * {i} = ".format(num=num,i=i),num*i)