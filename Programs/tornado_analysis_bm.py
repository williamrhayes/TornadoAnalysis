import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def main():

    df = pd.read_csv('tornadodata.csv').iloc[1588:]


    m = Basemap(resolution='h', projection='aeqd',
                lat_0=35.103216, lon_0=-92.221851,
                llcrnrlat=32, llcrnrlon=-95,
                urcrnrlat=38, urcrnrlon=-89,
                width=5000, height=5000)

    m.drawcoastlines()
    m.etopo()
    m.drawcountries(linewidth=2)
    m.drawstates(color='b')
    m.drawcounties(color='red')

    m.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')

    lrLat, lrLon = 34.746483, -92.289597
    myhouseLat, myhouseLon = 35.103216, -92.221851

    #xpt, ypt = m(myhouseLon, myhouseLat)
    #m.plot(xpt, ypt, 'c*')
    xpt, ypt = m(lrLon, lrLat)
    m.plot(xpt, ypt, 'c*')

    for row in df.iterrows():
        xpt, ypt = m(row[1].TouchdownLon, row[1].TouchdownLat)
        m.plot(xpt, ypt, 'r^')

    plt.title('Arkansas Tornadoes After 2008')
    plt.show()

main()

# Accomplished with reference to:

# https://basemaptutorial.readthedocs.io/en/latest/basemap.html
# https://www.youtube.com/watch?v=8v3how07th4