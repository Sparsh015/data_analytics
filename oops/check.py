class demo :
    a = 4

#before changing the value outside class
object = demo() 
print(object.a)

#after changing the value outside class
object.a = 10
print(object.a)

# CLASS attribute
print(demo.a)