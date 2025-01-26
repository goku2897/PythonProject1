#Python program to get the Fibonacci series between 0 to 50.
def printFibonaci_series(num):
    a = 0
    b = 1
    if num == 0:
      print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num+1):
            c = a+b
            a=b
            b=c
            if c > 50:
                break
            print(c)



num = int(input("enter a num: "))
printFibonaci_series(num)