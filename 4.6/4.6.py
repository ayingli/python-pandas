from pandas import read_csv

df = read_csv(
    'D:\\PDA\\4.6\\data.csv'
)

df['tel'] = df['tel'].astype(str)

#运营商
bands = df['tel'].str.slice(0, 3)
#地区
areas = df['tel'].str.slice(3, 7)
#号码段
nums = df['tel'].str.slice(7, 11)

#赋值回去
df['bands'] = bands
df['areas'] = areas
df['nums'] = nums
