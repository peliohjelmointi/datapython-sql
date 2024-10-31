import sqlite_connection as db
import pandas as pd
import csv 

connection = db.conn

# using Pandas:
df = pd.read_sql("SELECT * FROM MOVIES",connection)
df.to_csv("movies_as_csv.csv",index=False)


# cursor  = connection.execute("SELECT title,popularity \
#                           FROM movies \
#                           WHERE popularity >=20")

# # 1) Tallenna joka rivi listaan
# # 2) Tallenna listan data csv-tiedostoon csv.writer:illa

# lista = []
# for row in cursor:
#     lista.append(row)

# #print(lista)

# with open('suositut.csv','w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(lista)

# # print("HELLO", end=' ')
# # print("WORLD")



