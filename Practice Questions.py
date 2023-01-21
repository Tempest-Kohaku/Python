n = int(input("Enter the Maximum range of the Triangular Pattern : "))
for i in range(1,n) : 
    for j in range(i) : 
        print("*",end = " ")
    print(" ")
i = 1
j = 1
for i in range(n,0,-1) : 
    for j in range(i) : 
        print("*",end = " ")
    print(" ")
