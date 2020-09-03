# TornadoAnalysis
Analyzing severe weather patterns using data visualization and maps, specifically interested in Arkansas


I live in an area of Arkansas that frequently experiences tornado warnings and I'd like to 
know where the tornadoes have gone before! For this project I want to retrieve historical tornado 
data, plot it on a map, and determine how at-risk a given building is for tornadoes.


---------------------------------------------------------------
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 
Step 1: Retrieving data
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 

Thankfully, there are a number of open-source data repositories 
for tornado data! I will be using data from the tornado history
project's webpage:

http://www.tornadohistoryproject.com/tornado/Arkansas/map ,

which is labeled 

'tornadodata.csv'. 

This could then be easily loaded into my Python program,

'tornado_analysis_bm.py'

using the pandas read_csv method.

---------------------------------------------------------------
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 
Step 2: Using Basemap to Create the First Maps
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 

After installing Basemap, it was pretty easy to get started 
drawing maps. I followed the Basemap documentation and some 
additional Sentdex tutorials and was able to generate my first
map! I added state and county lines, colored the map, and 
added a title! 

After generating this map, I overlayed the touchdown position
of tornadoes that occurred after 2008 (whose coordinates have
more accuracy than those before). This allowed me to create the

'ArkansasTornadoesStartingPoints.png'

figure, which shows the starting points of over 300 tornadoes 
that affected Arkansas.

---------------------------------------------------------------
