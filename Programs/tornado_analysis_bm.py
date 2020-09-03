import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def main():

    # Read in the CSV file, .iloc gives us only
    # the tornadoes after 2008
    df = pd.read_csv('tornadodata.csv').iloc[1588:]

    # Create our map!
    m = Basemap(resolution='h', projection='aeqd',
                lat_0=35.103216, lon_0=-92.221851,
                llcrnrlat=32, llcrnrlon=-95,
                urcrnrlat=38, urcrnrlon=-89,
                width=5000, height=5000)

    # Draw political boundaries for reference
    m.drawcoastlines()
    m.drawcountries(linewidth=2)
    m.drawstates(color='b')
    m.drawcounties(color='red')

    # Color our map with topographical
    # information
    m.etopo()

    # Add the starting point of each tornado based
    # on its touchdown coordinates
    for row in df.iterrows():
        xpt, ypt = m(row[1].TouchdownLon, row[1].TouchdownLat)
        m.plot(xpt, ypt, 'r^')

    plt.title('Arkansas Tornadoes After 2008')
    plt.show()

main()

# Accomplished with reference to:

# https://basemaptutorial.readthedocs.io/en/latest/basemap.html
# https://www.youtube.com/watch?v=8v3how07th4