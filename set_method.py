demo_set1 = {"Delhi","Kolkata","Melbourne","Sydney"}
demo_Set2 = {"Delhi","Kolkata","Melbourne","Sydney","New York","Lucknow"}

#add
demo_set1.add("Gold Coast")
print(demo_set1)

#remove
demo_set1.remove("Delhi")
print(demo_set1)

#discard
demo_set1.discard("Delhi")
print(demo_set1)

#pop
demo_set1.pop()
print(demo_set1)

#Clear
demo_set1.clear()
print(demo_set1) #set()


#union
#It will join 2 set as set doesn't hold duplicate element
demo_Set3 = demo_set1.union(demo_Set2)
print(demo_Set3)

#update
# """It wont return a new set!"""
demo_set1.update(demo_Set2)
print(demo_set1)

#intersection :- keep only duplicate
demo_set3 = demo_set1.intersection(demo_Set2)
print(demo_set3)

demo_set1.intersection_update(demo_Set2)
print(demo_set1)


#symmertic_difference :- keep all excluding duplicate
demo_set3 = demo_set1.symmetric_difference(demo_Set2)
print(demo_set3)

demo_set1.symmetric_difference_update(demo_Set2)
print(demo_set1)

#difference() :- returns set containing difference betweeen two or more sets

demo_set3 = demo_set1.difference(demo_Set2)
print(demo_set3) #set()

demo_set1.difference_update(demo_Set2)
print(demo_set1) #set()

demo_set3 = demo_Set2.difference(demo_set1)
print(demo_set3) #{'Lucknow', 'New York'}

demo_Set2.difference_update(demo_set1)
print(demo_Set2) #{'Lucknow', 'New York'}


#issubset()
z= demo_set1.issubset(demo_Set2)
print(z) #True

# #issuperset()
z = demo_set1.issuperset(demo_Set2)
print(z) #False

z = demo_Set2.issuperset(demo_set1)
print(z) #True