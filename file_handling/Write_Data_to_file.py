# fp = open('/Users/rajeshpadhy/PycharmProjects/PythonProject1/file_handling/KG.txt','w')
# fp.write("Hello world,using for testing")
# fp.close()


fp = open('/Users/rajeshpadhy/PycharmProjects/PythonProject1/file_handling/KG_1.txt','w')
l = [56,79,50,60]

for item in l:
    fp.write(str(item)+'\n')

fp.close()