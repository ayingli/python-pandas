from pandas import DataFrame

df = DataFrame({
    'age': [21, 22, 23], 
    'name': ['KEN', 'John', 'JIMI']
})

df = DataFrame(
    data={
        'age': [21, 22, 23], 
        'name': ['KEN', 'John', 'JIMI']
    }, 
    index=['first', 'second', 'third']
)

#按列访问
df['age']

df[['age', 'name']]

#按行访问
df[1:2]

#按行索引访问
df.loc[['first', 'second']]

#按行列号访问
df.iloc[0:1, 0:1] 

#按行索引，列名访问
df.at['first', 'name']

#修改列名
df.columns
df.columns=['age2', 'name2']

#修改行索引
df.index
df.index = range(1,4)
df.index

#根据行索引删除
df.drop(1, axis=0)
#默认参数axis=0
#根据列名进行删除
df.drop('age2', axis=1)

#增加行，
#注意，这种方法，
#效率非常低，
#不应该用于遍历中
df.loc[len(df)] = [24, "KENKEN"]

#增加列
df['newColumn'] = [2, 4, 6]
