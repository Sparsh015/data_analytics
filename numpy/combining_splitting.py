import numpy as np

a1 = np.array([20,30,40])
b1 = np.array([15,16,17])

##### CONCATENATION 
print(np.concatenate([a1,b1]))

a2 = np.array([[20,30],[50,40]])
b2 = np.array([[15,16],[17,19]])
print(np.concatenate([a2,b2]))

#concatenate with axis and vertically one below other
print(np.concatenate([a2,b2], axis=0))
print(np.vstack([a2,b2]))

#concatenate with axis and horizontally side by side
print(np.concatenate([a2,b2], axis=1))
print(np.hstack([a2,b2]))

##### SPLIT
c = np.array([10,20,30,40,50])

d = np.array_split(c,3)
print(d)

#if number of splits are higher-> remaining will be formed as emoty arrays
print(np.array_split(c,7))
