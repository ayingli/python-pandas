import pandas

items = pandas.read_csv(
    'D:\\PDA\\4.12\\data1.csv', 
    sep='|', 
    names=['id', 'comments', 'title']
)

prices = pandas.read_csv(
    'D:\\PDA\\4.12\\data2.csv', 
    sep='|', 
    names=['id', 'oldPrice', 'nowPrice']
)

#默认只是保留连接上的部分
itemPrices = pandas.merge(
    items, 
    prices, 
    left_on='id', 
    right_on='id'
)

#即使连接不上，也保留左边没连上的部分
itemPrices = pandas.merge(
    items, 
    prices, 
    left_on='id', 
    right_on='id',
    how='left'
)

#即使连接不上，也保留右边没连上的部分
itemPrices = pandas.merge(
    items, 
    prices, 
    left_on='id', 
    right_on='id',
    how='right'
)

#即使连接不上，也保留所有没连上的部分
itemPrices = pandas.merge(
    items, 
    prices, 
    left_on='id', 
    right_on='id',
    how='outer'
)
