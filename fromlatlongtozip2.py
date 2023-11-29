# Import packages
from uszipcode import SearchEngine
# from uszipcode import Zipcode
import numpy as np
import zipfile
import pandas as pd
#Now to the real deal: the search function. This function can be #manually adapted to your needs (e.g., getting the full address instead of just ZIP codes)
search = SearchEngine()
NYPD_zip_file_path = 'Zipped_DS/NYPD_Complaint_Data_Historic.csv.zip'

crimes_csv_file_name = 'NYPD_Complaint_Data_Historic.csv'

with zipfile.ZipFile(NYPD_zip_file_path, 'r') as zip_ref:
    with zip_ref.open(crimes_csv_file_name) as file:
        df_crimes = pd.read_csv(file)


print(df_crimes[['Latitude', 'Longitude']].head(5))

def from_coordinates_to_zip(df):
    df = df[['Latitude', 'Longitude']]
    df_clean = df.dropna()

    l = []


zip = search.by_coordinates(40.828848, -73.916661, radius=10, returns=1)

print(zip)

