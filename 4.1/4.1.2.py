from pandas import read_table

df = read_table(
    'D://PDA//4.1//2.txt'
)
df

df = read_table(
    'D://PDA//4.1//2.txt', 
    names=['age', 'name'], 
    sep=','
)
df
