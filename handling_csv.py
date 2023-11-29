import pandas as pd
import zipfile
from Colonne import *

trees_zip_file_path = 'Zipped_DS/Trees.csv.zip'
NYPD_zip_file_path = 'Zipped_DS/NYPD_Complaint_Data_Historic.csv.zip'

trees_csv_file_name = 'Trees.csv'
crimes_csv_file_name = 'NYPD_Complaint_Data_Historic.csv'

with zipfile.ZipFile(trees_zip_file_path, 'r') as zip_ref:
    with zip_ref.open(trees_csv_file_name) as file:
        df_trees = pd.read_csv(file)

# with zipfile.ZipFile(NYPD_zip_file_path, 'r') as zip_ref:
#     with zip_ref.open(crimes_csv_file_name) as file:
#         df_crimes = pd.read_csv(file)

df_trees = df_trees[usefulcol_trees]

df_trees.to_csv('Trees.csv', index=True)