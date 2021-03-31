# -*- coding: utf-8 -*-

#生成一个整数的等差序列
#局限，只能用于遍历
r1_10 = range(1, 10, 2)

for i in r1_10:
    print(i)

r1_10 = range(0.1, 10, 2)


#生成一个小数的等差序列
import numpy
numpy.arange(0.1, 0.5, 0.01) 

r = numpy.arange(0.1, 0.5, 0.01) 

#向量化计算，四则运算
r + r
r - r
r * r
r / r

#函数式的向量化计算
numpy.power(r, 5)

#向量化运算，比较运算
r>0.3
#结合过滤进行使用
r[r>0.3]

#矩阵运算
numpy.dot(r, r.T)

sum(r*r)

from pandas import DataFrame
df = DataFrame({
    'column1': numpy.random.randn(5),
    'column2': numpy.random.randn(5)
})

df.apply(min)

df.apply(min, axis=1)

#判断每个列，值是否都大于0
df.apply(
    lambda x: numpy.all(x>0), 
    axis=1
)
#结合过滤
df[df.apply(
    lambda x: numpy.all(x>0), 
    axis=1
)]
