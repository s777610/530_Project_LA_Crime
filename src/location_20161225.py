import folium
import pandas


data = pandas.read_csv("Crime_Data_2010_2017.csv")
data_2016_1225 = data[data["Date Occurred"].str.contains('12/25/2016')]

victim_sex = data_2016_1225["Victim Sex"]
vic_is_M = victim_sex == "M"
vic_is_F = victim_sex == "F"

data_20161225_vic_M = data_2016_1225[vic_is_M]
data_20161225_vic_F = data_2016_1225[vic_is_F]

Location_M = list(data_20161225_vic_M["Location "])
Location_F = list(data_20161225_vic_F["Location "])


# create the map object, the location indicates starting view
map = folium.Map(location=[34.102461, -118.350515], zoom_start=10, tiles="Mapbox Bright")
# create the feature group
fg_crime_M = folium.FeatureGroup(name="Male Victim")
fg_crime_F = folium.FeatureGroup(name="Female Victim")

for location in Location_M:
    location_tuple = eval(location)
    # add child object to feature group, set the popup message
    # help(folium.CircleMarker) will show some info
    fg_crime_M.add_child(folium.CircleMarker(location=[location_tuple[0], location_tuple[1]],
                                             radius=3, fill_color="blue", fill=True, fill_opacity=0.7,
                                             color="blue"))

for location in Location_F:
    location_tuple = eval(location)
    fg_crime_F.add_child(folium.CircleMarker(location=[location_tuple[0], location_tuple[1]],
                                             radius=3, fill_color="red", fill=True, fill_opacity=0.7,
                                             color="red"))

# add feature group to map object
map.add_child(fg_crime_M)
map.add_child(fg_crime_F)
map.add_child(folium.LayerControl())

map.save("Map1.html")

