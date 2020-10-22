import folium

# Create map object
m = folium.Map(location=[50.4343, 30.5277], zoom_start=12)

# Global tooltip
tooltip = 'Click for more info'

# Create markers
folium.Marker([50.4494865, 30.6586025], popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m)

# Generate map in html
m.save('map.html')
