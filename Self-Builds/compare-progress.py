import numpy as np

#Writing a function that takes 2 NumPy arrays of equal length (e.g., marks in two subjects) and outputs a new array where:
#Value is "Improved" if element in B > A, "Dropped" if element in B < A and "Same" otherwise

mark1= input("enter old marks for 5 subjects")
arr1 = list(map(int, mark1.split()))
arr1 = np.array(arr1)

mark2= input("enter new marks for 5 subjects")
arr2 = list(map(int, mark2.split()))
arr2 = np.array(arr2)

result= np.full(5, "Same", dtype=object)

result[arr2 > arr1] = "Improved"
result[arr2 < arr1] = "Dropped"

print(result)
