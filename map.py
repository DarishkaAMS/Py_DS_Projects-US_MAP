import folium
import os
import json

# Create map object
m = folium.Map(location=[50.4343, 30.5277], zoom_start=12)

# Global tooltip
tooltip = 'Click for more info'

# Create custom marker icon
logoIcon = folium.features.CustomIcon('d_logo.png', icon_size=(50, 50))

# Vega data
vis = os.path.join('data', 'vis.json')

# Create markers
folium.Marker([50.4494865, 30.6586025], popup='<strong>Location One</strong>',
              tooltip=tooltip).add_to(m),

folium.Marker([50.4598435, 30.6487035], popup='<strong>Location Two</strong>',
              tooltip=tooltip, icon=folium.Icon(icon='leaf')).add_to(m),

folium.Marker([50.4698435, 30.6487035], popup='<strong>Location Two</strong>',
              tooltip=tooltip, icon=folium.Icon(icon='cloud', color='purple')).add_to(m),

folium.Marker([50.4398435, 30.6287035], popup='<strong>Location AMS</strong>',
              tooltip=tooltip, icon=logoIcon).add_to(m),

folium.Marker([50.4298435, 30.6687035], popup=folium.Popup(max_width=350)
              .add_child(folium.Vega(json.load(open(vis)), width=450, height=250))).add_to(m)

# Circle marker
folium.CircleMarker(
    location=[50.432043, 30.625697],
    radius=50,
    popup='Having Fun',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# Generate map in html
m.save('map.html')
