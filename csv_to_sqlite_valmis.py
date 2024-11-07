import sqlite3
from pathlib import Path
import pandas as pd

# CREATE EMPTY .DB FILE
Path('./databases/employees.db').touch() 

# CREATE DATABASE AND CURSOR
conn = sqlite3.connect('./databases/employees.db')
cursor = conn.cursor()

# CREATE TABLE WITH COLUMNS (see columns and types in .csv -file)
cursor.execute("CREATE TABLE IF NOT EXISTS all_employees (first_name TEXT, \
               last_name TEXT, \
               company_name TEXT \
               ,address TEXT \
               ,city TEXT \
               ,county TEXT \
               ,state TEXT \
               ,zip REAL \
               ,phone1 TEXT \
               ,phone2 TEXT \
               ,email TEXT \
               web TEXT )")

# LOAD DATA INTO PANDAS DATAFRAME
employees = pd.read_csv('./csv/us-500.csv')

# WRITE DATA TO SQLITE TABLE
employees.to_sql('all_employees', conn, if_exists='replace', index = True)