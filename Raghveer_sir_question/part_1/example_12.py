#Python program to display all numbers within a range except the prime numbers.

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
def display_num_except_primenumber(num):
    for i in range(num+1):
        if not isPrime(i):
            print(i)

num = int(input("enter a num"))
display_num_except_primenumber(num)

