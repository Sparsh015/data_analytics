class employee:
    a = 1 

class programmer(employee):
    b = 2

class manager(programmer):
    c = 3

o = employee()
print(o.a) # prints a attribute
#print(o.b) # error

o = programmer()
print(o.a , o.b) # prints a and b attribute

o = manager()
print(o.a , o.b , o.c) # prints a and b and c attribute

print(isinstance(o , programmer))
print(isinstance(o , employee))
print(isinstance(o , manager))

