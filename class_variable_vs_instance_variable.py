class RateOfInterest:

#instane variable case
#     def __init__(self,name,loan,interest):
#         self.name = name
#         self.loan = loan
#         self.interest = interest
#
#     def calc_interest(self):
#         print("Total Interest: ",self.interest * self.loan)
#
# p1 = RateOfInterest("Rajesh",500000,0.06)
# p1.calc_interest() #Total Interest:  30000.0
#
# p2 = RateOfInterest("Padhy",400000,0.06)
# p2.calc_interest() #Total Interest:  24000.0

#Class variable
#   interest = 0.06
#
#
#   def __init__(self, name, loan):
#         self.name = name
#         self.loan = loan
#
#
#   def calc_interest(self):
#        print("Total Interest: ",self.interest * self.loan)
#
# p1 = RateOfInterest("Rajesh",500000)
# p1.interest = 0.08 #Total Interest:  40000.0
# p1.calc_interest() #Total Interest:  30000.0
#
# p2 = RateOfInterest("Padhy",400000)
# p1.interest = 0.07 #Total Interest:  24000.0
# p2.calc_interest() #Total Interest:  24000.0


    interest = 0.06


    def __init__(self, name, loan):
        self.name = name
        self.loan = loan


    def calc_interest(self):
       print("Total Interest: ",self.interest * self.loan)


class Student(RateOfInterest):
    interest = 0.04

s = Student("Padhy", 100)
s.calc_interest()
