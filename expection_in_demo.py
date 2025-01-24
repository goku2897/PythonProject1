try:
 print("Input first number")
 x = int(input())
 print("Input second njmber")
 y = int(input())
 if y == 0:
     raise Exception("The denominator cannot be zero")
 print(x/y)

except Exception as e:
    print(e)
    print("In except block")

else:
    print("In else block") # else block will executed if there is no exception

finally:
    print("This is always executed")
