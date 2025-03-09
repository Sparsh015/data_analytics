class Car:
    def __init__(self , brand , model):
        self.brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + "!"

myCar = Car("Mercedes" , "S series")
print(myCar.brand)
print(myCar.model)
