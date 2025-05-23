class rectangle:
    def __init__(self):
        self.length = 10
        self.breadth = 5

rect = rectangle()
print("length", rect.length,"\nbreadth",rect.breadth)

class Square:
    def __init__(self,x):
        self.side = x

square = Square(15)
print(f"square side = {square.side}")

class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

circle = Circle(5)
print("radius = {}\t pi = {}".format(circle.radius,circle.pi))

#changing the global varirable of a class
Circle.pi = 3.14159
print("radius = {}\t pi = {}".format(circle.radius,circle.pi))

### adding a method to class
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

rect1 = Rectangle(10,5)
print("length = {} breadth = {} and area = {}".format(rect1.length,rect1.breadth,rect1.area() ))


#class metod and static method
class Circle:
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    #instance  method
    def cal_area(self):
        return Circle.pi * self.radius * self.radius

    
    #class method - cannotaccess radius
    @classmethod
    def access_pi(cls):
        pi = 3.143
        return pi
    
    #static method- cannot access pi and radius
    @staticmethod
    def circle_static():
        print("this is a static method")

circle = Circle(5)
print(circle.cal_area())         
print(Circle.access_pi())      
Circle.circle_static()         
