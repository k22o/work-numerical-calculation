import numpy as np
import scipy as sc
import scipy.linalg as sclinalg

str_dim = input('matrix size: dim = ')
dim = int(str_dim)

# 行列Aを乱数から生成する
np.random.seed(20200530)
mat_a = np.random.rand(dim, dim)

# 求めたいxの値, 求まるb
# x = [1,2,3,...]
vec_x = np.arange(1, dim+1)
vec_b = mat_a @ vec_x

##### 方法1: 逆行列を使う
inv_mat_a = sclinalg.inv(mat_a)
tmp_x = inv_mat_a @ vec_b
print(tmp_x)

##### 方法2: scipyの関数で解く
tmp_x = sclinalg.solve(mat_a, vec_b)
print(tmp_x)

##### 方法3: LU分解
mat_lu, pivot = sclinalg.lu_factor(mat_a)
tmp_x = sclinalg.lu_solve((mat_lu, pivot), vec_b)
print(tmp_x)
