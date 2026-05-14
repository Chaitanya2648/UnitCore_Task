# Importing NumPy library
import numpy as np

# Creating first NumPy array
arr1 = np.array([1, 2, 3])

# Printing the array
print(arr1)

# Finding index of element 3
index = np.where(arr1 == 3)

# Printing index
print("The index of element 3 is :", index[0][0])

# Finding square of each element
square = arr1 ** 2

print("Square:")
print(square)

# Finding mean of array
print("Mean:")
print(np.mean(arr1))

# Finding maximum value
print("Maximum:")
print(np.max(arr1))

# Finding minimum value
print("Minimum:")
print(np.min(arr1))

# Creating second array
arr2 = np.array([10, 20, 30])

# Addition of arrays
print("Addition:", arr1 + arr2)

# Subtraction of arrays
print("Subtraction:", arr2 - arr1)

# Multiplication of arrays
print("Multiplication:", arr1 * arr2)

# Division of arrays
print("Division:", arr2 / arr1)

# Creating matrices
matrix1 = np.array([[1, 2],
                    [3, 4]])

matrix2 = np.array([[5, 3],
                    [6, 7]])

# Matrix Addition
print("Matrix Addition:")
print(matrix1 + matrix2)

# Matrix Subtraction
print("Matrix Subtraction:")
print(matrix1 - matrix2)

# Matrix Multiplication
print("Matrix Multiplication:")
print(np.dot(matrix1, matrix2))