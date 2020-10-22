import folium

# Create map object
m = folium.Map(location=[50.4343, 30.5277], zoom_start=12)

# Generate map in html
m.save('map.html')
