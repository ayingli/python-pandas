import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.15\\data.csv', 
    sep='|'
)

bins = [
    min(data.cost)-1, 20, 40, 60, 
    80, 100, max(data.cost)+1
]

data['cut'] = pandas.cut(
    data.cost, 
    bins
)

data['cut'] = pandas.cut(
    data.cost, 
    bins, 
    right=False
)

labels = [
    '20以下', '20到40', '40到60', 
    '60到80', '80到100', '100以上'
]

data['cut'] = pandas.cut(
    data.cost, bins, 
    right=False, labels=labels
)
