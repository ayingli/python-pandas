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

mainColor = (42/256, 87/256, 141/256, 1);

mapData = pandas.DataFrame(basemap.states_info)

patches = []
for info, shape in zip(
    basemap.states_info, basemap.states
):        
    if info['NAME_1']=='Alabama':
        patches.append(
            Polygon(
                numpy.array(shape), True
            )
        )
ax.add_collection(
    PatchCollection(
        patches, facecolor=mainColor, 
        edgecolor=mainColor, 
        linewidths=1., zorder=2
    )
)

mainColor = (42/256, 87/256, 141/256, 1/2);

patches = []
for info, shape in zip(
    basemap.states_info, basemap.states
):
    if info['NAME_1']=='Minnesota':
        patches.append(
            Polygon(
                numpy.array(shape), True
            )
        )
ax.add_collection(
    PatchCollection(
        patches, facecolor=mainColor, 
        edgecolor=mainColor, 
        linewidths=1., zorder=2
    )
)


plt.show()