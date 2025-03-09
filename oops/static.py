class calculator :
    
    @staticmethod
    def hello():
        print("hello there")
    
    def __init__(self , num):
        self.num = num 

    @staticmethod
    def wait():
        print("...wait...")

    def square(self , num):
        print(f"the square is {self.num * self.num}")

    def cube(self,num):
        print(f"the cube is {self.num ** 3}")

    def sq_root(self,num):
        print(f"the square root is {self.num ** (1/2)}")

num = int(input("enter number "))

user = calculator(num)
user.hello()
user.wait()
user.square(num)
user.cube(num)
user.sq_root(num)
