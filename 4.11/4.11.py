from pandas import read_csv

df = read_csv(
    'D:\\PDA\\4.11\\data.csv', 
    sep=" ", 
    names=['band', 'area', 'num']
)

df = df.astype(str)

tel = df['band'] + df['area'] + df['num']

df['tel'] = tel
