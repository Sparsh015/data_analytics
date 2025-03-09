import numpy as np

a = np.array([[10,20],[30,40]])

#### APPEND -> append after convting to 1D
print(np.append(a,[50,60]))

#### INSERT
print(np.insert(a, 1, [25,35]))

#insert on multiple idxs
print(np.insert(a, [1,2], [25,35]))

#insert with axis
print("insert with axis = 1 \n",np.insert(a, 1, [25,35], axis = 1))
print("insert with axis = 0 \n",np.insert(a, 1, [25,35], axis = 0))


#### DELETE

#delete from idx after converting to 1d array
print("deletion from idx 1\n",np.delete(a,1))

#delete from axis (consider whole subarr in 2d)
print("deletion from axis= 0\n",np.delete(a,1, axis = 0))
print("deletion from axis= 1\n",np.delete(a,1, axis = 1))