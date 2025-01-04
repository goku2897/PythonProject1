demo_dict = {}
demo_dict = {1:20,2:45,3:50,6:67}
demo_dict2 = {"qa":"testurl","uat":"uaturl"}
demo_dict3 = {'qa':34,3:"uaturl"}
print(type(demo_dict)) #<class 'dict'>

print(demo_dict[6]) #67

print(demo_dict2['uat']) #uaturl

#How to add an element in the dict

demo_dict2['prod'] = 'produrl'

print(demo_dict2) #{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl'}

demo_dict2[1] = 56
print(demo_dict2) #{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl', 1: 56}

#pop
demo_dict2.pop(1)
print(demo_dict2) #{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl'}

# demo_dict2.pop() # we have to give some value when we use pop method
# print(demo_dict2)
