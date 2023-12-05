"""
Backend module for the FastAPI application.

This module defines a FastAPI application that serves
as the backend for the project.
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd


app = FastAPI()

# Accessing datasets from the drive folder

# Tourist attractions dataset
url_attractions = 'https://drive.google.com/uc?id=1a3DoOBChS0OgAsFVOFv5xnnfT6CTENDQ'

# Crime rate dataset
url_crime = 'https://drive.google.com/uc?id=1PWXz-4hPiEoKWLNJc-ArgB4ReiWshvRM'

# Underground stations dataset
url_stations = 'https://drive.google.com/uc?id=1hXbM2IKBm1libaYujJSfKLkqoekX4Pe5'

# Green areas dataset
url_trees = 'https://drive.google.com/uc?id=18B-D5PkjBZECkVUGGrnYymZjQBruCWj2'

# Neighbourhood and Zipcode dataset
url_zip = 'https://drive.google.com/uc?id=1lSuNA8ROF0MHA4GyWzpqUz3W1MsxI1g0'


# Creating dataframes with pandas
attractions = pd.read_csv(url_attractions)
crime = pd.read_csv(url_crime)
stations = pd.read_csv(url_stations)
trees = pd.read_csv(url_trees)
zip = pd.read_csv(url_zip)
bnb = pd.read_csv('backend/Datasets/AirBnb.csv')


# Deleting NaN from datasets
#attractions.fillna("", inplace=True)
#bnb.fillna("", inplace=True)


@app.get('/search')
def search_bnb(min, max):
    # Raggruppa per ZIP code e calcola il conteggio di attrazioni per ciascun ZIP code
    counts_by_zipcode = attractions.groupby('Zipcode')['Tourist_Spot'].count().reset_index()

    # Filtra i risultati in base a min_count e max_count
    filtered_zipcodes = counts_by_zipcode[(counts_by_zipcode['Tourist_Spot'] >= min) & (counts_by_zipcode['Tourist_Spot'] <= max)]

    # Restituisci la lista di ZIP code che soddisfano la condizione
    return filtered_zipcodes['Zipcode'].tolist()


list = search_bnb(0, 5, )
print(list  )





#print(bnb_df.head(1).to_dict(orient='records'))





def trasforma_prezzo(stringa):
    # Rimuovi il simbolo "$" e converti la stringa a float, quindi a intero
    return int(float(stringa.replace('$', '').replace(',', '')))

# Applica la funzione alla colonna "price" del DataFrame
bnb['price'] = bnb['price'].apply(trasforma_prezzo)

@app.get('/get_bnb')
def get_bnb(max_p = 500):
    dic = bnb[(bnb['price']) < max_p].to_dict(orient='records')
    
    return JSONResponse(content = dic)

@app.get('/print_first')
def print_first():
    prima_riga = attractions.head(1).to_dict(orient='records')
    return JSONResponse(content=prima_riga[0]['Tourist_Spot'])

# @app.get('/csv_show')
# def read_and_return_csv():
#     aux = df['Age'].values
#     return{"Age": str(aux.argmin())}

@app.get('/')
def read_root():
    """
    Root endpoint for the backend.

    Returns:
        dict: A simple greeting.
    """
    return {"Hello": "World"}




# @app.get('/query/{person_name}')
# def read_item(person_name: str):
#     """
#     Endpoint to query birthdays based on person_name.

#     Args:
#         person_name (str): The name of the person.

#     Returns:
#         dict: Birthday information for the provided person_name.
#     """
#     person_name = person_name.title()  # Convert to title case for consistency
#     birthday = birthdays_dictionary.get(person_name)
#     if birthday:
#         return {"person_name": person_name, "birthday": birthday}
#     else:
#         return {"error": "Person not found"}


# @app.get('/module/search/{person_name}')
# def read_item_from_module(person_name: str):
#     return {return_birthday(person_name)}


# @app.get('/module/all')
# def dump_all_birthdays():
#     return {print_birthdays_str()}


# @app.get('/get-date')
# def get_date():
#     """
#     Endpoint to get the current date.

#     Returns:
#         dict: Current date in ISO format.
#     """
#     current_date = datetime.now().isoformat()
#     return JSONResponse(content={"date": current_date})
