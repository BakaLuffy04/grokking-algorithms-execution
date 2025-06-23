import numpy as np

#Work with a 5x5 NumPy array of random integers from 1 to 100, and compute various statistics from it.

start = 1
stop = 100
arr = np.random.randint(start, stop+1, size=(5, 5))
mean = np.mean(arr, axis=1)
max_value = np.max(arr)
newarr = arr[arr > 50]
print("Array:\n", arr)
print("Shape:",arr.shape,"Mean:",mean,"Max:",max_value,">50",newarr)
