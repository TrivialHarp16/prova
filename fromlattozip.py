import pandas as pd
from geopy.geocoders import Nominatim
import geopy
from geopy.exc import GeocoderTimedOut
import zipfile
# Example DataFrame
NYPD_zip_file_path = 'Zipped_DS/NYPD_Complaint_Data_Historic.csv.zip'

crimes_csv_file_name = 'NYPD_Complaint_Data_Historic.csv'

with zipfile.ZipFile(NYPD_zip_file_path, 'r') as zip_ref:
    with zip_ref.open(crimes_csv_file_name) as file:
        df_crimes = pd.read_csv(file)

# # Define a reverse geocoding function
# def get_zipcode(lat, lon):
#     try:
#         geolocator = Nominatim(user_agent="convertlatintozip")
#         location = geolocator.reverse((lat, lon), exactly_one=True)
#         return location.raw['address']['postcode']
#     except GeocoderTimedOut:
#         return None

# # Apply the function to each row
# df_crimes['Zipcode'] = df_crimes.apply(lambda row: get_zipcode(row['Latitude'], row['Longitude']), axis=1)

# print(df_crimes)+

#df_crimes = df_crimes[["BORO_NM"]]

# col_to_check = ["Latitude", "Longitude"]

#df_crimes = df_crimes.dropna()

# def filter(list):
#     for element in list[:]:
#         if not element:
#             list.remove(element)
#     return list
# latitude = filter(latitude)
# longitude = filter(longitude)

#boro_counts = df_crimes['BORO_NM'].value_counts()

#print(boro_counts)

def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['postcode']



geolocator = geopy.Nominatim(user_agent='my_geocoder', timeout=10)

zipcodes = df_crimes.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field="Latitude", lon_field="Longitude")


df_crimes['ZipCode'] = zipcodes


# print(df_crimes.head())

#df_crimes.to_csv('Crimes.csv', index=True)