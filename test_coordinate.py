import pandas as pd
import math

class GeoCoords:
    def __init__(self, latitude, longitude):
        if not -90 <= latitude <= 90 or not -180 <= longitude <= 180:
            raise ValueError("Invalid latitude or longitude values")
        self.latitude = latitude
        self.longitude = longitude

def calculate_center(selected_attractions, csv_file = 'attractions.csv'):
    '''
    calculate_center return the center point given the coordinates of different attractions

    selected_attraction : list : str
        a list of all the selected attraction
    csv_file : str
        the path of the dataset containing the attractions name and their coordinates
    '''
    # Load data from CSV
    df = pd.read_csv(csv_file)

    # Filter the data for selected attractions
    filtered_df = df[df['Tourist_Spot'].isin(selected_attractions)]

    # Calculate the average latitude and longitude
    center_latitude = filtered_df['latitude'].mean()
    center_longitude = filtered_df['longitude'].mean()

    return GeoCoords(center_latitude, center_longitude)

def is_within_range(lat, lon, center, range):

    '''
    is_within_range checks if a given set of latitude and longitude is inside a given range from a given center

    Parameters
    ----------
    lat : float
        latitude of the location we want to check
    lon : float
        longitude of the location we want to check
    center : GeoCoords object
        the geographical coordinates of the central point of our search_area returned by the function "calculate_center"
    range : float
        the range of our search_area in degrees. 
    '''
    return center.latitude - range <= lat <= center.latitude + range and \
           center.longitude - range <= lon <= center.longitude + range

def find_airbnb_in_range(airbnb_list, center, range):
    in_range_airbnbs = []
    for airbnb in airbnb_list:
        if is_within_range(airbnb['latitude'], airbnb['longitude'], center, range):
            in_range_airbnbs.append(airbnb)
    return in_range_airbnbs



def dist_to_deg(dist, center):

    '''
    "dist_to_deg" will compute the degree variation in latitude that correspond to the meters inputted. 
    this result will be used as the search_range in the function "find_airbnb_in_range"

    Parameters
    ----------
    dist : int
        distance in meters that correspond to the radius of the search_area
    center : GeoCoords object
        the geographical coordinates of the central point of our search_area returned by the function "calculate_center"
    '''

    EARTH_RADIUS = 6378137  # Earth's radius in meters
    CIRCUMFERENCE = 2 * math.pi * EARTH_RADIUS  # Earth's circumference in meters
    conversion_factor = CIRCUMFERENCE * math.cos(math.radians(center.latitude)) / 360
    var_degree = dist / conversion_factor

    return var_degree


selected_attractions = ['Brooklyn Botanic Garden', 'Holographic Studios', 'Sleep No More']
center_point = calculate_center(selected_attractions)
print(f"Center Point: {center_point.latitude}, {center_point.latitude}")

# Function to extract ID from URL
def extract_id(url):
    return int(url.split('/')[-1])


if __name__ == "__main__":

    airbnb_dataset = pd.read_csv('AirBnb.csv')
    airbnb_list = [
                    {'id': extract_id(row['listing_url']), 
                    'latitude': row['latitude'], 
                    'longitude': row['longitude'], 
                    'zipcode': row['zipcode']
                    } for index, row in airbnb_dataset.iterrows()
                ]

    search_range = dist_to_deg(100, center_point)

    # Find Airbnb listings in range
    listings_in_range = find_airbnb_in_range(airbnb_list, center_point, search_range)

    for listing in listings_in_range:
        print(f"Airbnb ID: {listing['id']}, Latitude: {listing['latitude']}, Longitude: {listing['longitude']}, zipcode: {listing['zipcode']}")


