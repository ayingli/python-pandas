from pandas import Series

#定义，可以混合定义
x = Series(
    ['a', True, 1]
)

x = Series(
    ['a', True, 1], 
    index=['first', 'second', 'third']
)

#访问
x[1]
#根据index访问
x['second']

#不能越界访问
x[3]

#不能追加单个元素
x.append('2')
#追加一个序列
n = Series(['2'])
x.append(n)

x

#需要使用一个变量来承载变化
x = x.append(n)

'2' in x

#判断值是否存在
'2' in x.values

#切片
x[1:3]

#定位获取，这个方法经常用于随机抽样
x[[0, 2, 1]]

#根据index删除
x.drop(0)
x.drop('first')

#根据位置删除
x.drop(x.index[3])

#根据值删除
x['2'!=x.values]

