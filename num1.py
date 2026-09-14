import numpy as np
# the 1 d array.
my_array = np.arange(1,10)
print("1d Array:",my_array)

# reshaping the array into three*three matrix.
my_matrix = my_array.reshape(3,3)
print("\n3*3 Matrix:",my_matrix)

# creating an array of numbers 1 to 16
your_array = np.arange(1,17)
print("1d array:", your_array)

your_matrix = your_array.reshape(4,4)
print("\n4*4 matrix:", your_matrix)
# the using the subtraction in matrix.
sadda_array = np.arange(1,17)
print("1d array:", sadda_array)
sadda_matrix = sadda_array.reshape(4,4)
print("\n4*4 matrix:", sadda_matrix)

our_new_matrix = sadda_matrix-5
print("\n our new matrix:", our_new_matrix)

# the professional way of doing the matrix subtraction.
sadda_matrix = np.arange(1,17).reshape(4,4)
np.subtract(sadda_matrix,5,out = sadda_matrix)
print("\n sadda matrix:", sadda_matrix)