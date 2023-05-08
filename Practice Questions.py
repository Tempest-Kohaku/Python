n = int(input("Enter the Number : "))
tmp = n
reverse = 0
while n > 0 : 
    x = n%10
    reverse = (reverse * 10) + x
    n = n//10
print(f"The Reverse of {tmp} is {reverse}")