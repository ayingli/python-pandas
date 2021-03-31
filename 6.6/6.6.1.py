import numpy;
import matplotlib.pyplot as plt;
from matplotlib.patches import Polygon;
from mpl_toolkits.basemap import Basemap;
from matplotlib.collections import PatchCollection

#http://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap

'''
参数意义
llcrnrlon	
    所需的地图域（度）的左下角的经度。
llcrnrlat	
    所需的地图域（度）的左下角的纬度。
urcrnrlon	
    所需的地图域（度）的右上角的经度。
urcrnrlat	
    所需的地图域（度）的右上角的纬度。
'''

fig = plt.figure()
ax = fig.add_subplot(111)

basemap = Basemap(
    llcrnrlon=73.55770111084013, 
    llcrnrlat=18.159305572509766, 
    urcrnrlon=134.7739257812502, 
    urcrnrlat=53.56085968017586
)

chinaAdm1 = basemap.readshapefile(
    'D:\\PDA\\6.6\\china\\CHN_adm1', 
    'china'
)

mainColor = (42/256, 87/256, 141/256, 1);
cInfo = basemap.china_info
patches   = []
for info, shape in zip(basemap.china_info, basemap.china):
    if info['NAME_1']=='Liaoning':
        patches.append(
            Polygon(
                numpy.array(shape), 
                True
            )
        )

ax.add_collection(
    PatchCollection(
        patches, 
        facecolor=mainColor, 
        edgecolor=mainColor, 
        linewidths=1., 
        zorder=2
    )
)

mainColor = (42/256, 87/256, 141/256, 1/2);

patches   = []
for info, shape in zip(basemap.china_info, basemap.china):
    if info['NAME_1']=='Guangdong':
        patches.append(Polygon(numpy.array(shape), True))

ax.add_collection(
    PatchCollection(
        patches, 
        facecolor=mainColor, 
        edgecolor=mainColor, 
        linewidths=1., 
        zorder=2
    )
)

plt.show()