import numpy as np

#Build a tool that:
#Accepts two 3×3 matrices as input from the user (via CLI)
#Outputs:
#Matrix Addition
#Matrix Multiplication (dot product)
#Element-wise square of both matrices
#Transpose of each matrix


inp = input("Enter 9 space-separated values for Matrix 1: ")
arr = list(map(int, inp.split()))
matrix1 = np.array(arr).reshape(3, 3)


inp2 = input("Enter 9 space-separated values for Matrix 2: ")
arr2 = list(map(int, inp2.split()))
matrix2 = np.array(arr2).reshape(3, 3)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)

addition = matrix1 + matrix2
print("Addition:\n", addition)

mult = np.dot(matrix1, matrix2)
print("Multiplication:\n", mult)

sq1, sq2 = np.square(matrix1), np.square(matrix2)
print("square #1:\n", sq1, "\n", "square #2:\n", sq2)

t1, t2 = matrix1.T, matrix2.T
print("Transpose #1:\n", t1, "\n", "Transpose #2:\n", t2)
