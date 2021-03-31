from pandas import read_csv

df = read_csv(
    'D:\\PDA\\4.5\\data.csv'
)

newName = df['name'].str.lstrip()

newName = df['name'].str.rstrip()

newName = df['name'].str.strip()

df['name'] = newName
