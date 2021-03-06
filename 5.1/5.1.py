import pandas

data = pandas.read_csv(
    'D:\\PDA\\5.1\\data.csv'
)

data.score.describe()

data.score.size

data.score.max()

data.score.min()

data.score.sum()

data.score.mean()

data.score.var()

data.score.std()

#累计求和
data.score.cumsum()

#最大值和最小值所在位置
data.score.argmin()
data.score.argmax()

data.score.quantile(
    0.3, 
    interpolation="nearest"
)