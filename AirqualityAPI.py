import json
import requests
from datetime import datetime, timezone

#API CALL TO GET AIR QUALITY DURING A TIME SPAN
#http://api.openweathermap.org/data/2.5/air_pollution/history?lat={lat}&lon={lon}&start={start}&end={end}&appid={API key}


#test_brooklyn = "http://api.openweathermap.org/data/2.5/air_pollution?lat=40.6526006&lon=-73.9497211&appid=596dff3ac05aeb906e63803d2bfcf01a"
#test_manhattan = "http://api.openweathermap.org/data/2.5/air_pollution?lat=40.7896239&lon=-73.9598939&appid=596dff3ac05aeb906e63803d2bfcf01a"
#test_queens = "http://api.openweathermap.org/data/2.5/air_pollution?lat=40.7135078&lon=-73.828313&appid=596dff3ac05aeb906e63803d2bfcf01a"
#test_bronx = "http://api.openweathermap.org/data/2.5/air_pollution?lat=40.8466508&lon=-73.8785937&appid=596dff3ac05aeb906e63803d2bfcf01a"

average_brooklyn = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=40.6526006&lon=-73.9497211&start=946702800&end=1672549200&appid=596dff3ac05aeb906e63803d2bfcf01a"
#average_manhattan = "http://api.openweathermap.org/data/2.5/air_pollution/history?lat=40.7896239&lon=-73.9598939&start=946684800&end=1641058800&appid=596dff3ac05aeb906e63803d2bfcf01a"

#GEOCONVERTER
#test_2 = "http://api.openweathermap.org/geo/1.0/direct?q=Bronx&limit=1&appid=596dff3ac05aeb906e63803d2bfcf01a"

#response_brooklyn = requests.get(test_brooklyn)
#response_bronx = requests.get(test_bronx)
#response_manhattan = requests.get(test_manhattan)
#response_queens = requests.get(test_queens)

response_avg_brooklyn = requests.get(average_brooklyn)
#response_avg_manhattan = requests.get(average_manhattan)

#json_brooklyn = response_brooklyn.json()
#json_bronx = response_bronx.json()
#json_manhattan = response_manhattan.json()
#json_queens = response_queens.json()

json_avg_brooklyn = response_avg_brooklyn.json()
#json_avg_manhattan = response_avg_manhattan.json()

#print(json_brooklyn['list'][0]['main']['aqi'])
#print(json_bronx['list'][0]['main']['aqi'])
#print(json_manhattan['list'][0]['main']['aqi'])
#print(json_queens['list'][0]['main']['aqi'])

aqi_values = [entry['main']['aqi'] for entry in json_avg_brooklyn['list']]

mean_aqi = sum(aqi_values) / len(aqi_values)
print(len(aqi_values))
print("Mean AQI:", mean_aqi)
#print("-------")
#print(json_avg_manhattan)

'''
date_string = "2023-01-01 05:00:00"
date_format = "%Y-%m-%d %H:%M:%S"

# Convert the date string to a datetime object
dt_object = datetime.strptime(date_string, date_format)

# Convert the datetime object to a Unix timestamp
unix_timestamp = int(dt_object.replace(tzinfo=timezone.utc).timestamp())

print(f"The Unix timestamp for {date_string} is: {unix_timestamp}")
'''