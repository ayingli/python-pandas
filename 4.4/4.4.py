from pandas import read_csv

df = read_csv(
    'D:\\PDA\\4.4\\data.csv'
)

df = read_csv(
    'D:\\PDA\\4.4\\data2.csv',
    na_values=['a','b']
)


#找出空值的位置
isNA = df.isnull()


#获取出空值所在的行
df[isNA.any(axis=1)]

df[isNA[['key']].any(axis=1)]

df[isNA[['key', 'value']].any(axis=1)]

df.fillna('未知')

#直接删除空值
newDF = df.dropna()

