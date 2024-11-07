import sqlite3
from pathlib import Path
import pandas as pd

# LUO databases-kansioon UUSI TYHJÄ TIEDOSTO employees.db,  
Path('./databases/employees.db').touch()

# LUO sqlite-yhteys ja kursori luomaasi employees.db -tiedostoon
conn = sqlite3.connect('./databases/employees.db')
cursor = conn.cursor()
# Tutki us-500.csv -tiedostoa, ja LUO TAULU all_employees (MIETI KOLUMNIEN TIETOTYYPIT)
#  (vain jos taulua ei ole olemassa) 
"first_name","last_name","company_name","address","city","county","state","zip","phone1","phone2","email","web"
cursor.execute("""CREATE TABLE IF NOT EXISTS employees(
               first_name TEXT,
               last_name TEXT,
               company_name TEXT,
               address TEXT,
               city TEXT,
               county TEXT,
               state TEXT,
               zip INTEGER,
               phone1 TEXT,
               phone2 TEXT,
               email TEXT,
               web TEXT
               )""")


# #----------------------------------------------------------
# # LUO employees -niminen dataframe-tyyppinen muuttuja 
# # ja lue siihen us-500.csv -tiedoston sisältö

employees = pd.read_csv("./csv/us-500.csv")

# # MUUTA employees-dataframe SQL-MUOTOON employees.db -tiedostoon, 
# # all_employees-tauluun niin, että indeksi-sarake lisätään mukaan ja data yliajetaan, 
# # mikäli sitä löytyy

employees.to_sql('all_employees',conn, if_exists='replace', index=True)

# TIETOTYYPIT VOI OLLA ESIM. TEXT JA INTEGER (NUMEROT) katso apua 1.päivän csv_to_sqlite.py -tiedostosta

# from faker import Faker

# fake = Faker()
# print(fake.name())
# print(fake.address())
# print(fake.license_plate())
# print(fake.url())