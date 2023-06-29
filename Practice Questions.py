# Method - 1
# n = int(input("Enter the Number : "))
# i = 0
# for j in range(1,n+1) : 
#     triangle = ""  #Use it if you are going to use only one print statement 
#     for i in range(1,j+1) : 
#         triangle += str(i)
#         # print(i,end = "")
#     for num in range(i-1,0,-1) : 
#         triangle += str(num)
#         # print(num,end= "")
#     # print("")
#     print(triangle)

# Method - 2
# n = int(input("Enter the Number: "))
# for i in range(1, n+1):
#     pattern = [str(j) for j in range(1, i+1)]
#     pattern.extend([str(j) for j in range(i-1, 0, -1)])
#     print("".join(pattern))


# Method - 3
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    j = 1
    while j <= i:
        print(j, end='')
        j += 1
    j = i - 1
    while j >= 1:
        print(j, end='')
        j -= 1
    print()
