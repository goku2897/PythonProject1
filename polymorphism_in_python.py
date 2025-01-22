

#The word "Polymorphism" means having many format
# Same class method can work differently for different objects

#operatorn level

# x = 2
# y = 3
#
# print(x + y)
#
# x ="Rajesh "
# y = "Padhy"
#
# print(x + y)


#Function Level ploymorphism

#len

l = [1,2,3,4]

# print(len(l)) #4
#
# #l = "rajesh"
# print(len(l)) #6

print(sum(l))

def mul(*args) :

    total = 1
    for i in args:
        total *= i
    return total

print(mul(2,3))


class Human:
    def speak(self,language):
        print("I speak",language)

h1 = Human()
h1.speak("Hindi")

