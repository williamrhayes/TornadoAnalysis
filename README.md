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
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 
Step 3: Using the Maps to Show Tornado Paths
*** *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** 

The next step was plotting the ending points of the tornadoes!
To do this, we used the "Liftoff" latitude and longitude provided
in the data. Finally, a line was used to connect the tornadoes
(with a Fujita score greater than 0) to see the path that the 
tornadoes took.

Interestingly, I noticed that these tornadoes almost always travel
southwest to northeast. I wanted to see if this intuition was
correct so I decided to check if the latitude and longitude of the
ending point of the tornado was greater than the starting point.

To my surprise, I found that 88.95% of this time, this was the case!
This led me to believe that I was at the greatest risk of a tornado 
that starts to the southwest of my home.

A number of new figures are included in the "Figures" folder. Tornadoes
start at the red triangles and end at the yellow triangles. The 
thickness of the line connecting the triangle indicates the Fujita scale 
of the tornado. 

The next steps might be to change this line's thickness to scale with the
true path of destruction of the tornado, fixing the legend to be more readable,
and to include a scale for reference on the map.
