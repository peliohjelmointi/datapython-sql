import sqlite3
from sqlite3 import Error


# CTRL +K+C (COMMENT), CTRL +K+U (UNCOMMENT)
# TAI CTRL +' (TOGGLE COMMENTS ON/OFF)

#region Versio 1 

# try:
#     # sqlite3.connect luo tiedoston, jos polku on ok ja tiedostoa ei vielä ole
#     # mutta ei luo kansioita!, silloin menisi tässä except:iin
#     conn = sqlite3.connect("./databases/moviesDB.db")
#     if conn is None:
#         print("no connection")
#     else:
#         print("CONNECTION OK")

# except Error as e:
#     print(e)
#     conn = None
#endregion

#region Versio 2 (tarkistetaan polku)
import os # operating system, built-in module
db_path = "./databases/movies.db"

if os.path.exists(db_path): # vain jos muuttujan määrittämä löytyy
    conn = sqlite3.connect(db_path)
    print("db found and connected!")
else:
    print(f"can't connect to {db_path}")

#endregion
