a = (input("Enter the Number : "))
tmp = a
reverse = ''
print((a))
for i in range(len(a),0,-1) : 
    reverse += a[i-1]
    
    # x = a%10
    # reverse = (reverse * 10) + (x)
    # a = a//10
print(f"The Reverse of {tmp} is {reverse}")