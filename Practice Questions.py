list1 = list()
n = int(input("Enter the Number of the Elements in the List : "))
for i in range(n) : 
    a = int(input("Enter the Number to be Added in the List : "))
    list1.append(a)
maximum = list1[0]
minimum = list1[0]
for j in list1 : 
    if maximum < j : 
        maximum = j
    if minimum > j : 
        minimum = j
print(f"The Greatest Number is {maximum} and Smallest number is {minimum}")
