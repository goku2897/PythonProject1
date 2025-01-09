from random import choice

data = []
while True:
    input("Enter the name: ")
    data.append( input("Enter the name: "))

    choice = input("Enter another name ?? (y/n) :")
    if choice.casefold() == "n":
        break


for ele in data:
    print(ele,end=" ")
