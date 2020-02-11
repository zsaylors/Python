import folium
import pandas

# Creates map with initial coordinates
myMap = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles = "Stamen Terrain")

volcanoData = pandas.read_csv("Volcanoes.txt")
lat = list(volcanoData["LAT"])
lon = list(volcanoData["LON"])
elevation = list(volcanoData["ELEV"])
name = list(volcanoData["NAME"])

def colorProducer(elevation):
    if elevation < 3000:
        return "green"
    else:
        return "blue"

# Creates feature group and then adds coordinates to the feature group, then the map.
fgv = folium.FeatureGroup(name="Volcanos")
fgp = folium.FeatureGroup(name="Population")

for lt, ln, el, nm in zip(lat, lon, elevation, name):
    fgv.add_child(folium.Marker(location=[lt, ln], popup=nm + "\n" + str(el), icon=folium.Icon(color=colorProducer(el))))

fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), 
style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 100000000 else 'blue'}))

myMap.add_child(fgv)
myMap.add_child(fgp)
myMap.add_child(folium.LayerControl())
    
myMap.save("Map1.html")