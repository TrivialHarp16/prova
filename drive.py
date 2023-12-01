import pandas as pd
url='https://drive.google.com/file/d/1swsTIbqEsefGcuREjQrhJqbcKGoxdVJC/view?usp=drive_link'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
df = pd.read_csv(url)

print(df)