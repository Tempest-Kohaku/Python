# f = open('sample.txt','r')
# Use "open" Function To Read The Contents of the Files

f = open('sample.txt')  # By Default The Mode is 'r'
# data = f.read()
# Use 'read' Function to Read the contents of the Files
data = f.read(5)  # Reads 5 Elements from the txt Files
print(data)
f.close()