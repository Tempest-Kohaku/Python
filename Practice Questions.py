f = open('sample.txt','r')
# data = f.read()
data = f.read(5)
print(data)
f.close()