dict1 = dict()
for i in range(5) : 
    n = input("Enter the Key : ")
    m = []
    for i in range(5) :
        k = input("Enter the Values : ") 
        m.append(k)
    dict1[n] = m
    print("\n")
print(dict1)
print(dict1.keys())
print(dict1.values())

print(dict1.get("A"))
# for x in dict1.items() : 