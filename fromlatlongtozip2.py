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

df = df_crimes[['Latitude', 'Longitude']].head(1)
df_clean = df.dropna()

# zip = search.by_coordinates(40.828848, -73.916661, radius=10, returns=1)
# print(zip[0].zipcode)

def get_zipcode(row):
    result = search.by_coordinates(row['Latitude'], row['Longitude'], radius=10, returns=1)
    # Assuming the result has an attribute 'zipcode'
    return result[0].zipcode

df_clean['zipcode'] = df_clean.apply(get_zipcode, axis=1)

#df_crimes.to_csv('Crimes2.csv', index=True)

#print("ok")