demo_dict2 = {"qa":"testurl","uat":"uaturl"}


#get()
print(demo_dict2.get("preprod",0)) #preprodurl
#
# #keys()
# print(demo_dict2.keys()) #dict_keys(['qa', 'uat', 'preprod'])
#
# #items()
# print(demo_dict2.items()) #dict_items([('qa', 'testurl'), ('uat', 'uaturl'), ('preprod', 'preprodurl')])
#
# #values()
# print(demo_dict2.values()) #dict_values(['testurl', 'uaturl', 'preprodurl'])
#
# #pop()
# print(demo_dict2.pop("uat"))

# #popitem()
# print(demo_dict2.popitem())

#update()
# demo_dict2.update({"prod":"produrl"}) #{'qa': 'testurl', 'uat': 'uaturl', 'preprod': 'preprodurl', 'prod': 'produrl'}
# print(demo_dict2)

# demo_dict2.update({"preprod":"preprodbesturl"})
# print(demo_dict2) #{'qa': 'testurl', 'uat': 'uaturl', 'preprod': 'preprodbesturl'}

# #copy()
# demo_copy = demo_dict2.copy()
# print(demo_copy) #{'qa': 'testurl', 'uat': 'uaturl', 'preprod': 'preprodurl'}
#
# #clear()
# demo_copy.clear()
# print(demo_copy) #{}


