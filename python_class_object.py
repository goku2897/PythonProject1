class Employee:
    def __init__(self, fname,lname, email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def greet_person(self):
        print("Hello, Welcome to My Academy " +self.fname)

emp1 = Employee("Rajesh","Padhy","mv@rcvacademy.com")
print(emp1.fname)
emp1.greet_person()