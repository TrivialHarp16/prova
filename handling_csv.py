import pandas as pd
import zipfile
from Colonne import *

NYPD_zip_file_path = 'Zipped_DS/NYPD_Complaint_Data_Historic.csv.zip'

crimes_csv_file_name = 'NYPD_Complaint_Data_Historic.csv'


# with zipfile.ZipFile(NYPD_zip_file_path, 'r') as zip_ref:
#     with zip_ref.open(crimes_csv_file_name) as file:
#         df_crimes = pd.read_csv(file)
