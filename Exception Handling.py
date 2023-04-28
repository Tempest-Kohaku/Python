# Check whether the input is string or not
print("The First Program")
try : 
    a = int(input("Enter the Input : "))
    print("The Input given by the user is a Number")
except : 
    print("The Input given by the user is a String")

# Calculating the Median of the Given Raw Data
print("The Second Program")
b = list()
n = int(input("Enter the Length of the List : "))
try : 
    for i in range(n) : 
        num = int(input("Enter the Number to add in a list : "))
        b.append(num)
    print(b)
    if (n%2 == 0) : 
        ind1 = int((n+1)/2)
        l = b[ind1]
        m = b[ind1+1]
        median = (l+m)/2
        print("The Median of the given data in the list is : ",median)
    else : 
        ind2 = int((n+1)/2)
        median = b[ind2-1]
        print("The Median of the given data in the list is : ",median)
except : 
    print("There is an Error in the Program or the Input, Please Retry(O_o)>>>(@_@)")
    print("If the problem persist then go to the nearest Health/Eye checkup(>'_'<)")

# Lambda Function : Used to Carry out oneline operation i.e Small mathematical Operations
x=lambda z,y : z>y
print("sum=",x(60,200))
print("sum=",x(90,80))
