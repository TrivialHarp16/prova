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
        df_crimes = pd.read_csv(file, low_memory=False)


df_crimes.dropna(subset=['Lat_Lon'],inplace=True)
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

# def get_zipcode(df, geolocator, lat_field, lon_field):
#     location = geolocator.reverse((df[lat_field], df[lon_field]))
#     return location.raw['address']['postcode']



# geolocator = geopy.Nominatim(user_agent='my_geocoder', timeout=10)

# zipcodes = df_crimes.apply(get_zipcode, axis=1, geolocator=geolocator, lat_field="Latitude", lon_field="Longitude")


# df_crimes['ZipCode'] = zipcodes


# print(df_crimes.head())

#df_crimes.to_csv('Crimes.csv', index=True)

def convert_to_float_tuple(s):
    s = s.strip('()')
    parts = s.split(',')
    return float(parts[0]), float(parts[1])

df_crimes['Lat_Lon'] = df_crimes['Lat_Lon'].apply(convert_to_float_tuple)
from geopy.geocoders import Nominatim
from multiprocessing import Pool
import csv

# Sample coordinates (latitude, longitude)
coordinates = df_crimes['Lat_Lon'].to_list()

def get_zip_code(coord):
    geolocator = Nominatim(user_agent="testing_user")
    location = geolocator.reverse(coord, language="en", timeout=10)
    
    if location and location.raw.get("address"):
        zip_code = location.raw["address"].get("postcode")
        return zip_code
    else:
        return None

def parallelize_extraction(coordinates, num_processes=10):
    with Pool(num_processes) as pool:
        zip_codes = pool.map(get_zip_code, coordinates)
    return zip_codes

def save_to_csv(coordinates, zip_codes, filename="output.csv"):
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Latitude", "Longitude", "Zip Code"])
        for coord, zip_code in zip(coordinates, zip_codes):
            csv_writer.writerow([coord[0], coord[1], zip_code])

if __name__ == "__main__":
    result = parallelize_extraction(coordinates)
    save_to_csv(coordinates, result, filename="output.csv")
    print("Results saved to output.csv")