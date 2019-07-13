# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import os

os.chdir("C:/Users/gutie/Dropbox/Documentos Insumos/PREWORK_CGF/Module-4/Week6/Homework/")
# Import API key
from api_keys import api_key

# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy

# Output File (CSV)
output_data_file = "output_data/cities.csv"

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)


# List for holding lat_lngs and cities
lat_lngs = []
cities = []

# Create a set of random lat and lng combinations
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
len(cities)


url0= "http://api.openweathermap.org/data/2.5/weather?"
units = "imperial"
weather=pd.DataFrame()
# Build query URL
print("-----------------------------\nBegining Data Retrival\n-----------------------------")
for ct in range(len(cities)):
    city=cities[ct]
    url=url0+"appid="+api_key+"&units="+units+"&q="+city
    wresponse=requests.get(url)
    if wresponse.status_code != 200:
        print('City not found. Skipping...')
    elif wresponse.status_code == 200:
        print(f'Processing Record {ct} of Set {len(cities)} : {cities[ct]}')
        wjson=wresponse.json()
        weather=weather.append({"City":city,"Country":wjson['sys']['country'],"Latitud":wjson['coord']['lat'],"Longitud":wjson['coord']['lon'],
                                "Max Temperature":wjson['main']['temp_max'], "Humidity":wjson['main']['humidity'],
                                "Cloudiness":wjson['clouds']['all'], "Wind Speed":wjson['wind']['speed']}, ignore_index=True)
print("-----------------------------\nData Retrieval Complete\n-----------------------------")
    
plt.scatter(weather.Latitud, weather['Max Temperature'], marker="o", facecolors="#1d92cc",
            edgecolors="grey", alpha=0.50)
plt.ylim(0,weather["Max Temperature"].max()*1.1)
plt.xlim(weather["Latitud"].min()*1.1,weather["Latitud"].max()*1.1)
plt.title("City Latitude vs.Max Temperature (13/07/2019)")
plt.ylabel("Max.Temperature (°F)")
plt.xlabel("Latitude")
plt.grid(linestyle=":", color="#eb642f", linewidth=.5)

plt.savefig("Lat_Temperature.png")
plt.show()


##### Humidity
plt.scatter(weather.Latitud, weather['Humidity'], marker="o", facecolors="#1d92cc",
            edgecolors="grey", alpha=0.50)
plt.ylim(0,weather["Humidity"].max()*1.1)
plt.xlim(weather["Latitud"].min()*1.1,weather["Latitud"].max()*1.1)
plt.title("City Latitude vs. Humidity (13/07/2019)")
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(linestyle=":", color="#eb642f", linewidth=.5)

plt.savefig("Lat_Humidity.png")
plt.show()

### Cloudiness

plt.scatter(weather.Latitud, weather['Cloudiness'], marker="o", facecolors="#1d92cc",
            edgecolors="grey", alpha=0.50)
plt.ylim(-3,weather["Cloudiness"].max()*1.1)
plt.xlim(weather["Latitud"].min()*1.1,weather["Latitud"].max()*1.1)
plt.title("City Latitude vs.Cloudiness (13/07/2019)")
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(linestyle=":", color="#eb642f", linewidth=.5)

plt.savefig("Lat_Cloudiness.png")
plt.show()
    
#### Wind speed
plt.scatter(weather.Latitud, weather['Wind Speed'], marker="o", facecolors="#1d92cc",
            edgecolors="grey", alpha=0.50)
plt.ylim(0,weather["Wind Speed"].max()*1.1)
plt.xlim(weather["Latitud"].min()*1.1,weather["Latitud"].max()*1.1)
plt.title("City Latitude vs. Wind Speed(13/07/2019)")
plt.ylabel("Wind Speed (mph)")
plt.xlabel("Latitude")
plt.grid(linestyle=":", color="#eb642f", linewidth=.5)

plt.savefig("Lat_WindSpeed.png")
plt.show()