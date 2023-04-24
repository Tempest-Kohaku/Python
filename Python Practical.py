class A :
    def measures(self,x,y) : 
        self.x = x
        self.y = y
class B(A) :
    def areaRect(self) : 
        return self.x * self.y
a = int(input("Enter the Length of the Rectangle : "))
b = int(input("Enter the Breadth of the Rectangle : "))
area = B()
area.measures(a,b)
print("The Area of the Rectangle is : ",area.areaRect())
