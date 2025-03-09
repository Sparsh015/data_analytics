class employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"the \"class\" attribute of a is {cls.a}")

o = employee() 
o.a = 45

print(o.a)
o.show() 