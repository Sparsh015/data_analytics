class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def fuel_type(self):
        return "Petrol or Diesel"
        

class ElectricCar(Car):
    
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type():
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
Car("Tata", "Nexon")
my_car = Car("Toyota", "Corolla")

print(mycar.total_car)