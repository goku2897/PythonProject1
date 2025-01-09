# #
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *
# # * * * * *
#
#
# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()
#
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# # 1 2 3 4 5
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")
#     print()
#
# # 5 4 3 2 1
# # 5 4 3 2 1
# # 5 4 3 2 1
# # 5 4 3 2 1
# # 5 4 3 2 1
# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=" ")
#     print()
#
#
# """
# 11111
# 22222
# 33333
# 44444
# 55555
# """
#
# for i in range(1,6):
#     for j in range(1,6,1):
#         print(i,end=" ")
#     print()
# """
# 5 5 5 5 5
# 4 4 4 4 4
# 3 3 3 3 3
# 2 2 2 2 2
# 1 da1 1 1 1
# """
# for i in range(5,0,-1):
#     for j in range(1,6,1):
#         print(i,end=" ")
#     print()

n =int(input("Enter number of line: "))

m =int(input("Enter number of column: "))
for i in range(1,n):
    for j in range(1,m):
        print(i,end=" ")
    print()



