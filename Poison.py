n = int(input("Enter the Number : "))
def prime(a) : 
    flag = True
    for i in range(0,n+1) : 
        if i > 1 : 
            for num in range(2,i) : 
                if i%num == 0 : 
                    flag = False
                    break
                else : 
                    flag = True
    if flag == True : 
        print("It is a Prime Number")
    if flag == False : 
        print("Number is not a Prime Number")
prime(n)