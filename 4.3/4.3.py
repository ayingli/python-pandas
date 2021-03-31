from pandas import read_csv

df = read_csv('D://PDA//4.3//data.csv')

df

#找出行重复的位置
dIndex = df.duplicated()

#根据某些列，找出重复的位置
dIndex = df.duplicated('id')
dIndex = df.duplicated(['id', 'key'])

#根据返回值，把重复数据提取出来
df[dIndex]

#直接删除重复值
#默认根据所有的列，进行删除
newDF = df.drop_duplicates()
#当然也可以指定某一列，进行重复值处理
newDF = df.drop_duplicates('id')