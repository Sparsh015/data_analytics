class shape:
    def set_color(sel,color):
        sel.color = color
    
    def cal_area(self):
        return 100

    def color_shape(self):
        color_price = {"red":10, "blue":15, "green": 5}
        return self.cal_area()*color_price[self.color]
    
class Circle(shape):
    pi = 3.14
    def __init__(self,radius):
        self.radius = radius

    # overriding
    def cal_area(self):
        return Circle.pi * self.radius * self.radius

c = Circle(5)
c.set_color("red")

# here the area printed will be of the subclass not of the parent class
print("circle with radius = ", c.radius, "color = ", c.color, "cost = ",c.color_shape(), "area = ",c.cal_area())