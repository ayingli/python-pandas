import numpy
import pandas
import matplotlib
import Levenshtein
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection

font = {
    'family' : 'SimHei'
};
matplotlib.rc('font', **font);

fig = plt.figure()
ax = fig.add_subplot(111)


basemap = Basemap(
    llcrnrlon=73.55770111084013, 
    llcrnrlat=18.159305572509766, 
    urcrnrlon=134.7739257812502, 
    urcrnrlat=53.56085968017586
)
chinaAdm1 = basemap.readshapefile(
    'D:\\PDA\\6.6\\china\\CHN_adm2', 
    'china'
)

data = pandas.read_csv(
    'D:\\PDA\\6.6\\city.csv', 
    sep="\t"
)

data['scala'] = (
    data.population-data.population.min()
)/(
    data.population.max()-data.population.min()
)

mapInfo = basemap.china_info

suitSource=[]
suitTarget=[]
suitRatio=[]
def matchMapInfo(row):
    for info in basemap.china_info:
        if Levenshtein.ratio(info['NL_NAME_2'], row['city'])!=0:
            suitSource.append(row['city'])
            suitTarget.append(info['NL_NAME_2'])
            suitRatio.append(Levenshtein.ratio(info['NL_NAME_2'], row['city']))

data.apply(lambda row: matchMapInfo(row), axis=1)

suitDataFrame = pandas.DataFrame({
    'suitSource':suitSource, 
    'suitTarget':suitTarget, 
    'suitRatio':suitRatio
})

suitDataFrame = suitDataFrame.drop_duplicates();

suitDataFrame = suitDataFrame.sort(
    ['suitSource', 'suitRatio'], 
    ascending=[1, 0]
)

rnColumn = suitDataFrame.groupby(
    'suitSource'
 ).rank(
    method='first', 
    numeric_only=True, 
    ascending=False
)
suitDataFrame['rn'] = rnColumn

suitDataFrame = suitDataFrame[suitDataFrame.rn==1]

data = data.merge(
    suitDataFrame, 
    left_on="city", 
    right_on="suitSource"
)

def plotProvince(row):
    mainColor = (42/256, 87/256, 141/256, row['scala']);
    patches = []
    for info, shape in zip(basemap.china_info, basemap.china):        
        if info['NL_NAME_2']==row['suitTarget']:
            patches.append(Polygon(numpy.array(shape), True))
    ax.add_collection(
        PatchCollection(
            patches, facecolor=mainColor, 
            edgecolor=mainColor, linewidths=1., zorder=2
        )
    )

data.apply(lambda row: plotProvince(row), axis=1)

dataLoc = pandas.read_csv(
    'D:\\PDA\\6.6\\provinceLoc.csv'
)

def plotText(row):
    plt.text(
        row.jd, row.wd, row.city, 
        fontsize=14, fontweight='bold', 
        ha='center',va='center',color='r'
    )
    
dataLoc.apply(lambda row: plotText(row), axis=1)

plt.show()