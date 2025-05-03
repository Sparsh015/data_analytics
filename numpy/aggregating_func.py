import numpy as np
a = np.array([20,40,60,80])
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.size(a))
print(np.mean(a))
print(np.cumsum(a))
print(np.cumprod(a))

##for 2D

a1 = [100,150,199,200,250,130]
b1 = [10,50,30,40,30,10]

price = np.array(a1)
quantity = np.array(b1)

print(price , '\n',quantity)
print()

#to find the total cot of items use -> cumprod() for total cost of indivisual items and then
# then sum() for total cost
print(np.cumprod([price,quantity], axis = 0))

c = np.cumprod([price,quantity], axis = 0)
print(np.sum(c[1]))