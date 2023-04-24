dict1 = {
    "name":"john",
    "age":13
    }
print("Dictionary before the update : ")
print(dict1)
update_dict = {
    "friend" : "Manas",
    "Nigga" : "Rohan",
    "name" : "sakshi"}
dict1.update(update_dict)
print(dict1)
print("The Keys : ")
print(dict1.keys())
print("Values of the dictionay : ")
print(dict1.values())
print("Using the items function : ")
print(dict1.items())
print("Using the get function : ")
print(dict1.get("skate"))
# print(dict1["skate"])