import numpy
import pandas
import matplotlib
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
    llcrnrlon=-128,
    llcrnrlat=22,
    urcrnrlon=-64,
    urcrnrlat=53
)

usaAdm1 = basemap.readshapefile(
    'D:\\PDA\\6.6\\USA\\USA_adm1',
    'states', drawbounds=True
)
#人口数
data = pandas.read_csv(
    "D:\\PDA\\6.6\\data.csv"
)

mainColor = (42/256, 87/256, 141/256, 1);

data['2015 population'] = data[
    '2015 population'
].str.replace(",", "").astype(int)

data['scala'] = (
    data[
        '2015 population'
    ]-data[
        '2015 population'
    ].min()
)/(
    data[
        '2015 population'
    ].max()-data[
        '2015 population'
    ].min()
)

def plotProvince(row):
    mainColor = (
        42/256, 87/256, 141/256, 
        row['scala']
    )
    patches = []
    for info, shape in zip(
        basemap.states_info, basemap.states
    ):
        if info['NAME_1']==row['State']:
            patches.append(
                Polygon(
                    numpy.array(shape), 
                    True
                )
            )
    ax.add_collection(
        PatchCollection(
            patches, facecolor=mainColor, 
            edgecolor=mainColor, 
            linewidths=1., zorder=2
        )
    )

data.apply(lambda row: plotProvince(row), axis=1)

dataLoc = pandas.read_csv(
    'D:\\PDA\\6.6\\USALoc.csv'
)

def plotText(row):
    plt.text(
        row.Longitude, row.Latitude, row.State, 
        fontsize=14, fontweight='bold', 
        ha='center',va='center',color='r'
    )
    
dataLoc.apply(lambda row: plotText(row), axis=1)

plt.show()