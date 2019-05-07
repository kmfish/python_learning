# 内置函数创建ndarray
import numpy as np


def print_array(tag, x):
    print()
    print(tag + ":")
    print('X = \n', x)
    print()

    # We print information about X
    print('X has dimensions:', x.shape)
    print('X is an object of type:', type(x))
    print('The elements in X are of type:', x.dtype)


X = np.zeros((3, 4))
print_array("zeros", X)

b = np.ones((3, 5))
print_array('ones', b)

# 填充相同的元素
print_array('full', np.full((3, 4), 2))

# 单位矩阵
c = np.eye(3, 3)
print_array('eye', c)

# 对角矩阵
print_array("diag", np.diag([10, 20, 30, 50]))

# 给定区间内值均匀分布的ndarray
d = np.arange(10)
print_array('arange(10)', c)
e = np.arange(5, 10)
print_array("arange(5, 10)", e)
f = np.arange(5, 10, 2)
print_array("arange(5, 10, 2)", f)

# 步长可以是float
x = np.linspace(0, 25, 10)  # 这里包括了EndPoint 25
print_array("linspace", x)
x = np.linspace(0, 25, 10, endpoint=False)  # 这里不包括EndPoint 25
print_array("linspace", x)

# range & reshape
x = np.arange(20)
print_array('Original x = ', x)
x = np.reshape(x, (4, 5))  # 把一维的变为二维形状ndarray
print_array("Reshaped x = ", x)
Y = np.arange(20).reshape(4, 5)  # 可以连续写
print_array('Y', Y)

# random ndarray
# 创建给定形状的ndarray，包含位于半开区间[0.0, 1.0]的随机浮点数
x = np.random.random((3, 3))
print_array('random', x)
x = np.random.randint(4, 15, size=(3, 2))
print_array('random', x)

# 在某些情况下，你可能需要创建由满足特定统计学特性的随机数字组成的 ndarray。
# 例如，你可能希望 ndarray 中的随机数字平均值为 0。
# NumPy 使你能够创建从各种概率分布中抽样的数字组成的随机 ndarray。
# 例如，函数 np.random.normal(mean, standard deviation, size=shape) 会创建一个具有给定形状的 ndarray，
# 其中包含从正态高斯分布（具有给定均值和标准差）中抽样的随机数字。
# 我们来创建一个 1,000 x 1,000 ndarray，其中包含从正态分布（均值为 0，标准差为 0.1）中随机抽样的浮点数。
# We create a 1000 x 1000 ndarray of random floats drawn from normal (Gaussian) distribution
# with a mean of zero and a standard deviation of 0.1.
X = np.random.normal(0, 0.1, size=(1000, 1000))

# We print X
print()
print('X = \n', X)
print()

# We print information about X
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)
print('The elements in X have a mean of:', X.mean())
print('The maximum value in X is:', X.max())
print('The minimum value in X is:', X.min())
print('X has', (X < 0).sum(), 'negative numbers')
print('X has', (X > 0).sum(), 'positive numbers')
