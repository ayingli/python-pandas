# -*- coding: utf-8 -*-
import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.17\\data.csv', 
    encoding='utf8'
)

dateparse = lambda dates: pandas.datetime.strptime(
    dates, '%Y%m%d'
)

data = pandas.read_csv(
    'D:\\PDA\\4.17\\data.csv', 
    encoding='utf8',
    parse_dates=['date'],
    date_parser=dateparse,
    index_col='date'
)

#根据索引进行抽取
import datetime

dt1 = datetime.date(year=2016,month=2,day=1);
dt2 = datetime.date(year=2016,month=2,day=5);

data.ix[dt1: dt2]

data.ix[[dt1,dt2]]

#根据时间列进行抽取
data = pandas.read_csv(
    'D:\\PDA\\4.17\\data.csv', 
    encoding='utf8',
    parse_dates=['date'],
    date_parser=dateparse,
)

data[(data.date>=dt1) & (data.date<=dt2)]
