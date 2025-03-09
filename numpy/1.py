import numpy as np

lst = [1,2,3,4,5]
arr = np.array(lst)

print(lst)
print(arr)
print(type(arr))

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
lst3 = [11,12,13,14,15]

#multidimen array created
arr1 = np.array([lst1,lst2,lst3])
print(arr1)

#print number of (rows, cols) 
print(arr1.shape)

#reshape the array from (n , m) to (m , n)
print(arr1.reshape(5,3))

#datatype of arr
print(arr.dtype)

#to convert from one data type to another
print(arr.astype(float))

#indexing in multidimen array
print(arr1[ : , 1])
print(arr1[1: ,1:3])

# creating new arrays
new_arr = np.arange(1,10,2)  
print(new_arr)

new_arr2 = np.arange(1,20,2).reshape(2,5)
print(new_arr2)

one_matrix = np.ones((5,3))

zero_matrix = np.zeros((5,2))

print(one_matrix)
print(zero_matrix)

#true false value for entire array
print(arr<2)

#specific element for value less than 2
print(arr[arr<2])

