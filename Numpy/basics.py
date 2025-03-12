import numpy as np

x = np.array([1, 2, 3]);
y = np.array([1, 2, 3], dtype='float32');

# 2 x 3 matrix
z = np.array([[1, 2, 3], [4, 5, 6]]);

# print(z);
# print(np.full((3,3), 9)); # scalar matrix of 9
# print(np.zeros((3,3))); # zero matrix
# print(np.ones((3,3))); # ones matrix
# print(np.random.rand(3,3)); # random matrix

# print(np.eye(3, k=2)); # identity matrix, k = diagonal offset
# print(np.diag([1,2,3])); # diagonal
# print(np.arange(0, 10, 2)); # range
# print(np.linspace(1, 10, 5)); # linear space, 5 elements between 0 and 10

""" Different dimensions of ndarray """
np_arr = np.array([[1,2,3], [4,5,6]]);
# print(np_arr);
# print(np_arr.ndim); # number of dimensions
# print(np_arr.shape); # shape of the array
# print(np_arr.size); # total number of elements

""" Reshape """
# print(np_arr.reshape(3,2)); # reshape to 3 x 2 matrix 💡: -1 for auto calculation
# print(np_arr.flatten()); # flatten the array, but it is a deep copy
# print(np_arr.ravel()); # flatten the array, but it is a shallow copy

""" Transpose """
# print(np_arr.transpose()); # transpose the array 💡: np_arr.T

""" Slicing & Indexing """
# print(np_arr[0, 1]); # first row, second column
# print(np_arr[:, 1]); # all rows, second column
# print(np_arr[1, :]); # second row, all columns
# print(np_arr[1, 0:2]); # second row, first two 

""" Flipping """
# print(np.flip(np_arr, axis=0)); # reverse the rows

""" Concatenation & Stacking """
a = np.array([[1,2], [3,4]]);
b = np.array([[5,6], [7,8]]);
# print(np.concatenate((a, b), axis=1)); # concatenate along rows

# print(np.hstack((a, b))); # horizontal stack
# print(np.vstack((a, b))); # vertical stack

""" Mathematical Operations """
# Using broadcasting, we can apply simple arithmetic operations on numpy arrays with different shapes.

# print(a + b); # element-wise addition
# print(a - b); # element-wise subtraction
# print(a * b); # element-wise multiplication
# print(a / b); # element-wise division

# print(np.mean(a)); # mean of the array
# print(np.median(a)); # median of the array
# print(np.std(a)); # standard deviation of the array

# print(np.sum(a)); # sum of the array
print(np.sum(a, axis=0)); # sum along the rows