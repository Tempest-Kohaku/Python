list = [10,20,60,30,20,40,30,60,70,80]
exist = {}
print(type(exist))
duplicates = []
for i in list : 
    if i not in exist : 
        exist[i] = 1
    else : 
        duplicates.append(i)
    print(duplicates)
    print("\\")
    print(exist)
    print("\\")