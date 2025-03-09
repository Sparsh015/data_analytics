import numpy as np

a1 = np.array([7,8,13,9,14])
a2 = np.array([[7,8,13,9,14],[5,17,14,6,4]])

######### SORTING ##########

###### SORT
print(np.sort(a1))
print(np.sort(a2))

##### WHERE
print(np.where(a1==9))
print(np.where(a2==13))

print(np.where(a2 % 2 == 0))

##### SEARCHSORTED -> need an soreted array for operations
ar = np.array([1,2,3,4,5])
print(np.searchsorted(ar,3))



######## FILTERING #########

arr = np.array([20,30,40,50])
fa1 = [True,False,True,False]

print(arr[fa1])

fa2 = arr>32
print(arr[fa2])

arr2 = np.array([20,30,40,50,60])
fa3 = arr % 6 != 0
print(arr[fa3])



