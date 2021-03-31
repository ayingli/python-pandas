
from pandas import DataFrame;

df = DataFrame({
    'age': [21, 22, 23], 
    'name': ['KEN', 'John', 'JIMI']
})

df.to_csv(
    "D:\\PDA\\4.2\\df.csv"
)

df.to_csv(
    "D:\\PDA\\4.2\\df.csv", 
    index=False
)
