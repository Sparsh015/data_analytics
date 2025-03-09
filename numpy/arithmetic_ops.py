import numpy as np
import math
a = np.array([[30,40],[20,10]])
b = np.array([[30,20],[10,20]])

# addition of arrays
print(a+b)
print(np.add(a,b))

# subtraction
print(a-b)
print(np.subtract(a,b))

# multiplication
print(a*b)
print(np.multiply(a,b))

# division
print(a/b)
print(np.divide(a,b))

a1 = np.array([3,4,2,1])
b1 = np.array([2])

# power function
print(np.pow(a1,b1))
print(a1**b1)

a2 = np.array([144, 36, 81, 9])

# sqrt functn
print(np.sqrt(a2))
print(np.sqrt(a2).astype(int)) #converted to int since sqrt returns float

