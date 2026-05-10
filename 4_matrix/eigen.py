import numpy as np
import scipy.linalg as sclinalg

mat_a = np.array([[2,2],[[1,1]]])
eigval, eigvec = sclinalg.eig(mat_a)

print('Eigenvalue: ', eigval)
print('Eigenvectors: = ', eigvec)