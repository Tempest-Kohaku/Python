list1 = [12,75,150,180,145,525,50]
for i in range(len(list1)) : 
    if list1[i] > 500 : 
        break
    elif list1[i] > 150 : 
        continue
    elif list1[i]%5 == 0 : 
    	print(list1[i])