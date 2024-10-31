import sqlite_connection as db
import pandas as pd

connection = db.conn

df = pd.read_sql("SELECT title FROM movies LIMIT 10", connection)
df.to_csv("ekat_10.csv",index=False)

