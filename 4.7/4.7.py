from pandas import read_csv

df = read_csv(
    'D:\\PDA\\4.7\\data.csv'
)

newDF = df['name'].str.split(' ', 1, True)

newDF.columns = ['band', 'name']
