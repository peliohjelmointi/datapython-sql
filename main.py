import sqlite_connection as db

connection = db.conn

cursor  = connection.execute("SELECT title,popularity \
                          FROM movies \
                          WHERE popularity >=20")

# kaikki hakutulokset cursorista
    #for row in cursor:
    #   print(row)

# haetaan vain ensimmäinen tulos
result = cursor.fetchone()
print(result)

result = cursor.fetchone() # siirtyy seuraavaan
print(result)
#print(result)

#kokeillaan hakea seuraava tulos
iteraattori = iter(cursor)
rivi = next(iteraattori) #next siirtyy indexissä yhdellä eteenpäin
rivi2 = next(iteraattori)
print(rivi2)


# Suosittelen aina käyttämään!
connection.close()
 
