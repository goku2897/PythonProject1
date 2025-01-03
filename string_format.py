x = "Python class"
y = "Rcv Academy"

print("Welcome to "+x+" from " +y) #
print("Welcome to %s from %s" %(x,y)) #Welcome to Python class from Rcv Academy

print("Welcome to %s from %s"%("Java Class",y)) #Welcome to Java Class from Rcv Academy

print("Welcome to {1} from {0}".format(x,y)) # Welcome to Rcv Academy from Python class

print("Welcome to {1} from {0}".format(y,x)) #Welcome to Python class from Rcv Academy

print("Welcome to {classnane} from {academy}".format(classnane=x,academy=y)) #Welcome to Python class from Rcv Academy