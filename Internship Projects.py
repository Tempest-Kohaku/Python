# Example : "Create four lists (l1, l2, l3, l4) and four sets (s1, s2, s3, s4).
# Combine the lists into a single list containing only the elements that are present in all four lists
#  Also, create a set (s) that contains all the unique elements from the four sets.
# Print both the combined list and the set."
l1 = [21,4,12,1,7,23,16,18,19]
l2 = [13,24,17,2,9,21,4,13,14,43,35]
l3 = [21,4,12,1,7,23,16,18,19]
l4 = [25,32,28,21,31,4,38,41,84,91]
s1 = {1,2,23,45,36,47,3,12,57}
s2 = {23,56,34,78,23,1,41,31}
s3 = {1,2,23,45,36,47,3,12,57}
s4 = {76,67,23,12,78,14}

s = s1 | s2 | s3 | s4
print(s)

l = list()
for m in l1 : 
    if m in l2 and m in l3 and m in l4 : 
        l.append(m)
print(l)
