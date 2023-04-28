import threading # import the thread module
import time # import time module  
def cal_sqre(num): # define the cal_sqre function
    print("Calculate the Square of the Given Number")
    for n in num : 
        if n%2 == 0 : 
            time.sleep(0.3) # at each iteration it waits for 0.3 time
            print('Square is : ', n**2)
def cal_cube(num) : # define the cal_cube() function
    print("Calculate the Cube of  the Given Number")
    for n in num : 
        if n%2 != 0 :     
            time.sleep(0.3) # at each iteration it waits for 0.3 time
            print("Cube is : ", n**3)
# arr = [4, 5, 6, 7, 2] # given array
n = int(input("Enter the Length of the List : "))
arr = list()
for i in range(n) : 
    a = int(input("Enter the Element of the Array : "))
    arr.append(a)
t1 = time.time() # get total time to execute the functions
cal_sqre(arr) # call cal_sqre() function
cal_cube(arr) # call cal_cube() function
print("Total time taken by threads is :",time.time() - t1) # print the total time