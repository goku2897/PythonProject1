fp = open('/Users/rajeshpadhy/PycharmProjects/PythonProject1/file_handling/KG.txt','r')
# print(fp.read()) #read all the text
#print(fp.readline(3)) #Hel
# print(fp.readlines())

# for data in fp.readlines():
#     print(data)  # Hello world,using for testing , To learn testing concept

for data in range(0,3):
     print(fp.readline())
fp.close()