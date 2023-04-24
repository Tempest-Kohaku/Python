def fact(num) : 
    if num ==0 or num == 1 : 
        return 1
    return num * fact(num-1)
n = int(input("Enter the Number : "))
print("Factorial of the given Number is : ",fact(n))