import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def display_on_map(city, lat, lon):
    fig = plt.figure(num=None, figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='tan', lake_color='lightblue')
    # draw parallels and meridians.
    m.drawparallels(np.arange(-90., 91., 30.), labels=[True, True, False, False], dashes=[2, 2])
    m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, False, False, True], dashes=[2, 2])
    m.drawmapboundary(fill_color='lightblue')
    plt.title("Mercator Projection")

    # Map (long, lat) to (x, y) for plotting
    x, y = m(lon,lat)
    plt.plot(x, y, 'bo', markersize=5)
    plt.text(x, y, ' '+city, color='blue', fontsize=10);
    plt.show()


