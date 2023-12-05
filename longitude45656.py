import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

# Load the dataset
attractions_df = pd.read_csv("/Users/simonedilorenzo/prova/Datasets/locations.csv")

# Initialize the geolocator
geolocator = Nominatim(user_agent="tesst344", timeout=10)

# Function to get latitude and longitude
def get_lat_lon(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        return get_lat_lon(address)

# Apply the function to each row
attractions_df['latitude'], attractions_df['longitude'] = zip(*attractions_df['Address'].apply(get_lat_lon))

# Save the updated dataframe
attractions_df.to_csv('updated_attractions.csv', index=False)