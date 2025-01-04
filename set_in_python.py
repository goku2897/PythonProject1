#unorder colllection with no duplicate element
# set is specified with {}

demo_set1 = {10,20,30,40,40}
demo_set5 = demo_set1
print(demo_set5)
demo_set2 = {10,20,30,40,40.5}
demo_set3 = {"10","20"}
demo_Set4 = set(("45",45,"67",65))

print(demo_set1)
print(demo_Set4)
print(len(demo_set2)) #5
print(20 in demo_set2) #True
print("20" in demo_set2) #False
#in the case for empty set we should use set() not {}