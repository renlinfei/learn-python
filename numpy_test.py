import numpy as np

# arr1 = np.array([2, 3, 4])
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.1, 2.2, 3.3])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1 + arr2)
#
# print(arr2 * 10)
# data = np.array([[1, 2, 3], [4, 5, 6]])
# print(data)
# print(data.dtype)
#
# print(np.zeros((3, 5)))
# print(np.ones((4, 6)))
# print(np.empty((2, 3, 5)))

# print(np.arange(10))
#
# arr4 = np.arange(10)
# print(arr4[5])
# print(arr4[4 : 8])

arr5 = np.arange(10)
# arr5[5:8] = 15
# print(arr5)
arr_slice = arr5[5:8].copy()
arr_slice[:] = 10
print(arr5)
print(arr_slice)






