#Python program to check if a given number is an Armstrong number



def check_Armstrong(num):
    temp = num
    length = len(str(temp))
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit ** length
        num = num // 10
    return sum == temp
num = 153
if check_Armstrong(num):
    print("The number is Armstrong")
else:
    print("The number is not Armstrong")