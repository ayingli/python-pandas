import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.13\\data.csv', 
    sep="|"
)

data['total'] = data.price*data.num

#注意，用点的方式，虽然可以访问，但是并没有组合进数据框中
data = pandas.read_csv(
    'D:\\PDA\\4.13\\data.csv', 
    sep="|"
)

data.total = data.price*data.num
