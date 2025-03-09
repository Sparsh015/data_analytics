class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the \"class\" attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.__fname} {self.__lname}"

    @name.setter
    def name(self,value):
        self.__fname = value.split(" ")[0]
        self.__lname = value.split(" ")[1]

o = employee() 
o.a = 45
print(o.a)

o.name = "Sparsh Mahajan"

print(o.fname , o.lname)

o.show() 