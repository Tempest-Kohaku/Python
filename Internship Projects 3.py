while True : 
    choice = input("Enter your choice for programming example\n1. List\t\t2. Set\n3. Function\t4. Constructor\n : ")

    if choice == "List" or choice == "1" : 
    # Example : Finding Maximum and Minimum Element of a List
        print("Program 1 on List : ")
        l1 = []
        n = int(input("Enter the Length of the List : "))
        for i in range(n+1):
            a = int(input("Enter the Elements of the List : "))
            l1.append(a)
        print(l1)
        max_number = l1[0]
        min_number = l1[0]
        for num in l1 : 
            if num > max_number:
                max_number = num
            if num < min_number:
                min_number = num
        print(f"Maximum number : {max_number}")
        print(f"Minimum number : {min_number}")

    # Example : Add Even Number in the List in range 0,50
        print("Program 2 on List : ")
        l2 = list()
        for m in range(0,51) : 
            if m%2 == 0 : 
                l2.append(m)
        print(l2)

    # Example : Print List in Reverse Order
        print("Program 3 on List : ")
        l3 = [32,56,12,1,67,21]
        for k in range(len(l3),0,-1) : 
            k = k - 1
            print(l3[k])
        break

    elif choice == "Set" or choice == "2" : 
    # Example : Return a new set of identical items from two sets
        print("Program 1 on Sets : ")
        set1 = {10,20,30,40,50,21,54}
        set2 = {30,40,50,60,70,21,23}
        print(set1.intersection(set2))

    # Example : Get Only unique items from two sets
        print("Program 2 on Sets : ")
        s1 = {10,20,30,27,32,40,50,70,36}
        s2 = {30,40,50,60,82,32,21,27,70}
        print(s1.union(s2))

    # Example : Update set1 by adding items from set2, except common items
        print("Program 3 on Sets : ")
        set1 = {10,20,30,40,50}
        set2 = {30,40,50,60,70}
        print(set1.union(set2))
        break
    elif choice == "Function" or choice == "3" : 
    # Example : Create a function with a default argument
        print("Program 1 on Functions : ")
        def Greet(name = "Naruto") : 
            print("Hello, Good Morning ",name)
        Greet("Hinata")
        Greet()
        
    # Example : Factorial of the Number
        print("Program 2 on Functions : ")
        def fact(n):
            if n == 0:
                return 1
            else:
                return n * fact(n - 1)
        n1 = int(input("Enter the Number : "))
        print(f"Factorial of {n1} is : {fact(n1)}")

    # Example : Add two Numbers
        print("Program 3 on Functions : ")
        def add(a,b):
            return a + b
        n1 = float(input("Enter the First number : "))
        n2 = float(input("Enter the Second number : "))
        result = add(n1,n2)
        print("The sum is:",result)
        break
    elif choice == "Constructor" or choice == "4" : 
    # Example : Name and Age of the Person
        print("Program 1 on Constructor : ")
        class Person:
            def __init__(self,name,age):
                self.name = name
                self.age = age
        p1 = Person("Aman Pandey",19)
        print("Name : ",p1.name)
        print("Age : ",p1.age)

    # Example : Details about a book
        print("Program 2 on Constructors : ")
        class Book:
            def __init__(self,title,author,year):
                self.title = title
                self.author = author
                self.year = year
        book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
        print("Title:", book1.title)
        print("Author:", book1.author)
        print("Year:", book1.year)

    # Example : Mathematical Operation on Rectangle
        print("Program 3 on Constructors : ")
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height
            def area(self):
                return self.width * self.height
            def perimeter(self):
                return 2 * (self.width + self.height)
        rectangle1 = Rectangle(4, 6)
        print("Width:", rectangle1.width)
        print("Height:", rectangle1.height)
        print("Area:", rectangle1.area())
        print("Perimeter:", rectangle1.perimeter())
        break    
    else : 
        print("Invalid Choice, Please Choose a Valid Choice")
    break