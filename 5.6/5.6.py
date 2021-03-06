# -*- coding: utf-8 -*-
import pandas

data = pandas.read_csv(
    'D:\\PDA\\5.6\\data.csv'
)

#先来看看如何进行两个列之间的相关度的计算
data['人口'].corr(data['文盲率'])

#多列之间的相关度的计算方法
#选择多列的方法
data[[
    '超市购物率', '网上购物率', '文盲率', '人口'
]]

data[[
    '超市购物率', '网上购物率', '文盲率', '人口'
]].corr()
