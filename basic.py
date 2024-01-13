import numpy as np
matrix = np.array([[1,2,3],[4,5,6]])
vector=np.array([7,9,6])
print('matrix:\n',matrix)
print('vector:\n',vector)
print('matrix.shape:',matrix.shape)
print('vector.shape:',vector.shape)
print('matrix.dtype:',matrix.dtype)
print('vector.dtype:',vector.dtype)
print('matrix.size:',matrix.size)
print('vector.size:',vector.size)
print('matrix.ndim:',matrix.ndim)
print('vector.ndim:',vector.ndim)
print('matrix.itemsize:',matrix.itemsize)
print('vector.itemsize:',vector.itemsize)
print('matrix.nbytes:',matrix.nbytes)
print('vector.nbytes:',vector.nbytes)
print('matrix.T:\n',matrix.T)
print('vector.T:\n',vector.T)
print('matrix.flatten():',matrix.flatten())
print('vector.flatten():',vector.flatten())
print('matrix.reshape(3,2):\n',matrix.reshape(3,2))
print('vector.reshape(3,1):\n',vector.reshape(3,1))
print('matrix.reshape(3,-1):\n',matrix.reshape(3,-1))
print('vector.reshape(-1,1):\n',vector.reshape(-1,1))
print('matrix.reshape(-1,1):\n',matrix.reshape(-1,1))
print('vector.reshape(-1,1):\n',vector.reshape(-1,1))
