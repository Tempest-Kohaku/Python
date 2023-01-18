n = int(input("Enter the Number : "))
tmp = n
sum = 0
while n > 0 : 
    i = n%10
    sum += (i**3)
    n = n//10
if tmp == sum : 
    print("The Number given is an Armstrong Number")
else : 
    print("The Number given is not an Armstrong Number")