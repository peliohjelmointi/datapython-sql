import sqlite_connection as db
import pandas as pd
from pathlib import Path 

# Create empty file
Path('leffat.db').touch()

# Create db connection
connection = db.conn

# Create db cursor
cursor = connection.cursor()

# Create table with columns (only if table does not already exist)
cursor.execute("CREATE TABLE IF NOT EXISTS movies  \
          (id INT, \
          title TEXT, \
          overview TEXT, \
          popularity REAL , \
          release_date TEXT, \
          vote_average REAL , \
          vote_count INT)")

# Load cursor data into panda dataframe
movie_data = pd.read_csv('movies_as_csv.csv')

# Write movie_data into sqlite table
                 #table   #connection #what to do       # index or not
movie_data.to_sql('movies',connection, if_exists='append',index=False)