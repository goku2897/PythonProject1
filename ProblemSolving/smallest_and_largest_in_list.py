n = int(input("enter the total no of element you want inside your list"))

l = []
for i in range(n):
   l.append(int(input("enter the element you want inside your list")))
print(l)
print("minimum element is {min} and Maximum element is {max}".format(min=min(l), max=max(l)))
