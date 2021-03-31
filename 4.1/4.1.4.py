# coding UTF-8
from pandas import read_table

#OSError: Initializing from file failed

filePath = 'D://PDA//4.1//中文.txt'

df = read_table(
    filePath, 
    sep=',', 
    encoding='UTF-8'
)

df = read_table(
    filePath, 
    sep=',', 
    encoding='UTF-8', 
    engine='python'
)

df
