#Python program to find the factorial of a given number.
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


results = fact(int(input("Enter a number: ")))
print(results)


