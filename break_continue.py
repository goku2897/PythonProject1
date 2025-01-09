# x= 0
# while x < 10:
#     print(x)
#     x+=1
#     continue
#     print("inside the the loop")
# print("outside of the loop")

# x= 0
# y= 0
# while x < 10:
#     print(x)
#     x+=1
#     print("Parent loop")
#     while y<5:
#         print(y)
#         y+=1
#         break
#         print("Inner loop")
# print("outside of the loop")


x = 0
while x < 10:
    print(x)
    x += 1
    if x == 5:
        break
else:
    print("out of the while loop")
