import json
import urllib.request
import pandas as pd

# Take data as a url
# Use top level object or function
# display data
# Use relevant columns which are community_villages, water functionality
# Filter data by number of water points that are functional
# Group by number of water points per community
# Rank community by percentage of btoken water points

geourl = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

response = urllib.request.urlopen(geourl)
content = response.read()
data = json.loads(content.decode("utf8"))
print(type(data))
