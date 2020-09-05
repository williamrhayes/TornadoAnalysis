import pandas as pd
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

def main():

    # Read in the CSV file, .iloc gives us only
    # the tornadoes after 2008
    df = pd.read_csv('tornadodata.csv').iloc[1588:]

    # Choose the latitude and longitude that the
    # map is centered around (Little Rock in this case)
    lat, lon = 34.746483, -92.289597

    # Size of the map
    range = 0.75

    # Create our map!
    m = Basemap(resolution='c', projection='aeqd',
                lat_0=lat, lon_0=lon,
                llcrnrlat=lat-range, llcrnrlon=lon-range,
                urcrnrlat=lat+range, urcrnrlon=lon+range)

    # Draw political boundaries for reference
    m.drawcoastlines()
    m.drawcountries(linewidth=4)
    m.drawstates(color='b')
    m.drawcounties(color='red')

    # Color our map with topographical
    # information
    #m.etopo()

    lrLat, lrLon = 34.746483, -92.289597

    xpt, ypt = m(lrLon, lrLat)
    m.plot(xpt, ypt, 'g*')


    # Add the starting point of each tornado based
    # on its touchdown coordinates
    upright_count = 0
    for row in df.iterrows():
        tornado = row[1]

        # If the tornado starts within the map boundaries,
        # plot it!
        if (tornado.Fujita > 0 and tornado.LiftoffLat != "-" and
            tornado.TouchdownLon > m.llcrnrlon and
            tornado.TouchdownLon < m.urcrnrlon and
            tornado.TouchdownLat > m.llcrnrlat and
            tornado.TouchdownLat < m.urcrnrlat):

            # Plot where the tornado touched down
            xpt1, ypt1 = m(tornado.TouchdownLon, tornado.TouchdownLat)
            m.plot(xpt1, ypt1, 'r^')

            # Plot where the tornado lifted off
            xpt2, ypt2 = m(float(tornado.LiftoffLon), float(tornado.LiftoffLat))
            m.plot(xpt2, ypt2, 'y^')

            # Connect the start and end of the tornado
            m.plot([xpt1, xpt2], [ypt1, ypt2],
                    linewidth=tornado.Fujita,label=tornado.Date)

    # Add a legend to track down the tornadoes
    plt.legend(title='Tornadoes', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.title('Arkansas Tornadoes After 2008')
    plt.show()

main()

# Accomplished with reference to:

# https://basemaptutorial.readthedocs.io/en/latest/basemap.html
# https://www.youtube.com/watch?v=8v3how07th4
# https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot