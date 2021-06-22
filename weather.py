import requests
#import os
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather = ("Current weather desc  :",api_data['weather'][0]['description'])

hmdt =("Current Humidity      :",str(api_data['main']['humidity']),"%")
wind_spd = ("Current wind speed    :",str(api_data['wind']['speed']),'kmph')
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
f=open('comic.txt','w') 
   
f.write("-------------------------------------------------------------")
f.write("Weather Stats for - {}  || {}".format(location.upper(), date_time))
f.write("-------------------------------------------------------------")

f.write("Current temperature is: {:.2f} deg C".format(temp_city))
f.write(''.join(weather))
f.write(''.join(hmdt))
f.write (''.join(wind_spd))
f.close()