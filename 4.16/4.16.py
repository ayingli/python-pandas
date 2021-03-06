import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.16\\data.csv', 
    encoding='utf8'
)

data['时间'] = pandas.to_datetime(
    data.注册时间, 
    format='%Y/%m/%d'
)

data['格式化时间'] = data.时间.dt.strftime('%Y-%m-%d')

data['时间.年'] = data['时间'].dt.year
data['时间.月'] = data['时间'].dt.month
data['时间.周'] = data['时间'].dt.weekday
data['时间.日'] = data['时间'].dt.day
data['时间.时'] = data['时间'].dt.hour
data['时间.分'] = data['时间'].dt.minute
data['时间.秒'] = data['时间'].dt.second
    
