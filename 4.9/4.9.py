# -*- coding: utf-8 -*-
import numpy
import pandas

data = pandas.read_csv(
    'D:\\PDA\\4.9\\data.csv'
)


#设置随机种子
numpy.random.seed(seed=2)


#按照个数抽样
data.sample(n=10)
#按照百分比抽样
data.sample(frac=0.02)
#是否可放回抽样，
#replace=True，可放回, 
#replace=False，不可放回
data.sample(n=10, replace=True)


#典型抽样，分层抽样
gbr = data.groupby("class")

gbr.groups

typicalNDict = {
    1: 2, 
    2: 4, 
    3: 6
}

def typicalSampling(group, typicalNDict):
    name = group.name
    n = typicalNDict[name]
    return group.sample(n=n)

result = data.groupby(
    'class', group_keys=False
).apply(typicalSampling, typicalNDict)



typicalFracDict = {
    1: 0.2, 
    2: 0.4, 
    3: 0.6
}

def typicalSampling(group, typicalFracDict):
    name = group.name
    frac = typicalFracDict[name]
    return group.sample(frac=frac)

result = data.groupby(
    'class', group_keys=False
).apply(typicalSampling, typicalFracDict)
