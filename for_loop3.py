#Ask a number from user. Print all the numbers from 1 to that number
from itertools import count

# num = int(input("Enter a number: "))
#
#
# for i in range(num):
#     print(i)
# # for i in range(1,num+1):
# #     print(i)


#Ask a number n from user. Print all the numbers from N to 1

# num = int(input("Enter a number: "))
#
# for i in range(num,0,-1):
#     print(i)


#Ask start number and end number from user. Print all the numbers

# start_num = int(input("Enter start number: "))
# end_num = int(input("Enter end number: "))
#
# for i in range(start_num, end_num + 1):
#     print(i)


#Calculate the sum of all the number from 1 to 10

# total = 0
# for i in range(1,11):
#     total= total+i
# print(total)

#Calculate how many numbers are divisible by 7 from 1 to 100

# count = 0
# for i in range(1,101):
#     if i%7 == 0:
#         count = count+1
# print(count)

#Calculate how many number are divisible by both 6 and 7 between 1 to 200.

# count = 0
# for i in range(1,200):
#     if i%6 ==0 and i%5 == 0:
#         count = count+1
# print(count)


#Calculate the sum of all the number are divisible by 4 between 20 to 50.

total_sum = 0
for i in range(20,50):
    if i%4 == 0:
        total_sum+=i
print(total_sum)