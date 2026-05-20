import numpy as np

# to create an array
arr1 = np.array([1,2,3,4,5])
print(arr1) 

# to find the index of number
index_num = arr1[3]
print("the index of the given number is:", index_num)

# to find the square of the given list
sq_num = arr1 ** 2
print("the sqaure of the given list is:", sq_num) 

# to find the cube of the given list
cube_num = arr1 ** 3
print("the cube of the given list is:", cube_num) 

# to find the square root of the given list
sqrt_num = np.sqrt(arr1)
print("the sqaure root of the given list is:", sqrt_num) 

# to find the mean value of the given list
mean_num = arr1.mean()
print("the mean value of the given list is:", mean_num)

# maximum number from the given list 
max_value = arr1.max()
print("the maximum value from the list is:", max_value)

# minimum number from the given list
min_value = arr1.min()
print("the minimum value from the given list is:", min_value)

# median number from the given list
mid_value = np.median(arr1)
print("the median value from the given list is:", mid_value)

# creating another list for performing mathematical operations
arr2 = [6,7,8,9,10]

# addition of the value in the given list
add_val = arr1 + arr2
print("the addition of the given two list is:", add_val)

# subtraction of the value in the given list
sub_val = arr1 - arr2
print("the subtracion of the given two list is:", sub_val)

# multiplication of the value in the given list
mul_val = arr1 * arr2
print("the multiplication of the given two list is:", mul_val)

# division of the given value in the given list
div_val = arr1 / arr2
print("the division of the given two list is:", div_val)

# modulus of the given value in the list 
mod_val = arr1 % arr2
print("the modulus of the given two list is:", mod_val)

# creating a matrix
matrix1= np.array([[1, 2, 3],
                  [4, 5, 6]])
print(matrix1)

matrix2= np.array([[2, 4, 6],
                  [8, 10, 12]])
print(matrix2)

# to find the diminsion of the matrix 1
shape_mat = np.shape(matrix1)
print("the dimensions of the matrix 1 is:", shape_mat)

# to find the number of dimensions of the matri 1
dim_mat = np.ndim(matrix1)
print("the dimensions of the given matrix is:", dim_mat)

# addition of the 2 matrix
add_mat = matrix1 + matrix2
print("the addiion of the two matrix is:", add_mat)

# subraction of the 2 matrix
sub_mat = matrix1 - matrix2
print("the subtraction of the two matrix is:", sub_mat)

# multiplication of the matrix
mul_mat = matrix1 * matrix2
print("the multiplication of the given matrix is:", mul_mat)

# transpose of the matrix
T_mat = np.transpose(matrix1)
print("the transpose od the given matrix is:", T_mat)

# the division of the given matrix
div_mat = matrix1 / matrix2
print("the division of the given matrix is:", div_mat)