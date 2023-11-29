import pandas as pd
import zipfile
from Colonne import *

zip_file_path = 'Trees.csv.zip'
csv_file_name = 'Trees.csv'

with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    with zip_ref.open(csv_file_name) as file:
        df = pd.read_csv(file)

df = df[usefulcol_trees]

print(df.head())