import numpy as np
import numpy.matlib
import random

import pandas as pd

from pandas import Series,DataFrame

if __name__ == '__main__':
    #数组
    # a = [1, 2, 3, 4, 5, 6]
    # b = np.array(a)
    # c = b.reshape(3, 2)
    # print(c)

    # print("平均值%f" % c.mean())
    
    
    # print(np.zeros((6, 9)))
    # print(np.ones((2, 5)).shape)
    
    # print(np.random.randint(5, 10))
    # print(np.random.rand(4, 4) * 100)

    # 矩阵
    x = np.matrix([[1, 2, 3], [4, 5, 6]])
    print(x)
    print(x.T)

    print(x[0, 2])
    y = np.matlib.zeros((2, 3))
    print(y)

    z = np.matlib.identity(4)
    print(z)
    print(np.matlib.rand((4, 4)))

    A = np.matrix([[1, 2, 3], [4, 3, 6]])
    B = np.matrix([[1, 2], [3, 4], [5, 6]])
    print(A)
    print()
    print(A.trace())
    print(A * B)

    print(pd.Series([11, 12], index=["北京", "上海"]))
    print(pd.Series((4, 9)))
    
    # pandas常用方法

    
    
    
    

    
    
    
    
    