import pandas as pd

def calculate_center(csv_file, selected_attractions):
    # Load data from CSV
    df = pd.read_csv(csv_file)

    # Filter the data for selected attractions
    filtered_df = df[df['Tourist_Spot'].isin(selected_attractions)]

    # Calculate the average latitude and longitude
    center_latitude = filtered_df['latitude'].mean()
    center_longitude = filtered_df['longitude'].mean()

    return center_latitude, center_longitude

class GeoCoords:
    def __init__(self, latitude, longitude):
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError("Invalid latitude or longitude values")
        self.latitude = latitude
        self.longitude = longitude

def get_coordinates(position, n_range):
    in_range = []
    lat_start = max(-90, position.latitude - n_range)
    lat_end = min(90, position.latitude + n_range)
    lon_start = max(-180, position.longitude - n_range)
    lon_end = min(180, position.longitude + n_range)

    lat_step = 0.00000000000001  # Smaller step for more precision
    lon_step = 0.00000000000001  # Smaller step for more precision

    current_lat = lat_start
    while current_lat <= lat_end:
        current_lon = lon_start
        while current_lon <= lon_end:
            in_range.append(GeoCoords(current_lat, current_lon))
            current_lon += lon_step
        current_lat += lat_step

    return in_range

def is_within_range(lat, lon, center, range):
    return center.latitude - range <= lat <= center.latitude + range and \
           center.longitude - range <= lon <= center.longitude + range

def find_airbnb_in_range(airbnb_list, center, range):
    in_range_airbnbs = []
    for airbnb in airbnb_list:
        if is_within_range(airbnb['latitude'], airbnb['longitude'], center, range):
            in_range_airbnbs.append(airbnb)
    return in_range_airbnbs

# Example Airbnb dataset
# airbnb_dataset = [
#     {'id': 1, 'latitude': 40.721, 'longitude': -73.981},
#     {'id': 2, 'latitude': 40.722, 'longitude': -73.989},
#     # ... more listings ...
# ]

airbnb_dataset = pd.read_csv("/Users/simonedilorenzo/prova/Datasets/AirBnb_Listing.csv")
# Define the center and range
central_position = GeoCoords(40.722414066666666, -73.98609163333333)
search_range = 0.000000001  # 0.01 degrees in latitude and longitude

# Find Airbnb listings in range
listings_in_range = find_airbnb_in_range(airbnb_dataset, central_position, search_range)

for listing in listings_in_range:
    print(f"Airbnb ID: {listing['id']}, Latitude: {listing['latitude']}, Longitude: {listing['longitude']}")
# # Example usage
# selected_attractions = ['Brooklyn Botanic Garden', 'Holographic Studios', 'Sleep No More']
# center_point = calculate_center('/Users/simonedilorenzo/prova/Datasets/attractions.csv', selected_attractions)
# print("Center Point:", center_point)

# position = GeoCoords(40.722414066666666, -73.98609163333333)
# ranges = get_coordinates(position, 0.0000000000001)

# for cords in ranges:
#     print(f"{cords.latitude}, {cords.longitude}")



