from operator import ge
import sqlite3

# class Database:
# def __init__(self,db):
#     self.conn = sqlite3.connect(db)
#     self.cur = self.conn.cursor()
#     self.cur.execute(
#         "CREATE TABLE IF NOT EXISTS albums (id INTEGER PRIMARY KEY, artist_name text, album_name text,year text, genre text)")
#     self.conn.commit()

# def add_album(self, artist,album,year,genre):
#     self.cur.execute("INSERT INTO albums VALUES (NULL, ?, ?, ?, ?)", (artist, album, year, genre))
#     self.conn.commit()

# def fetch_albums(self):
#     self.cur.execute("SELECT * FROM albums")
#     rows = self.cur.fetchall()
#     result = []
#     for row in rows:
#         result.append(
#             str(row[0]) +
#             "-" +
#             str(row[1]) +
#             '-' +
#             row[2] +
#             '-' +
#             row[3] +
#             '-' +
#             str(row[4]))
#     return result


# def remove(self, selected_album):
#     self.cur.execute("DELETE FROM albums WHERE id=?", (selected_album[0],)) #needs comma, because is tuple
#     self.conn.commit()

# def update(self,selected_album,artist,album,year,genre):
#     print(id)
#     self.cur.execute("UPDATE albums SET artist_name = ?, album_name = ?, year = ?, genre = ? WHERE id = ?",
#      (artist,album,year,genre,selected_album[0]))
#     self.conn.commit()

# def __del__(self): #destructor call when all instances of object has been deleted
#     self.conn.close()

# db = Database('albums.db')
# db.add_album("Deep Purple", "In Rock", "1970", "Rock")


# ---------------WITH FUNCTIONS ONLY---------------------------

conn = sqlite3.connect("albums.db")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS albums (id integer primary key, artist_name text, album_name text,year text, genre text)"
)
conn.commit()


def add_album(artist, album, year, genre):

    #id = get_max_id() + 1
    
    cur.execute("INSERT INTO albums VALUES (NULL,?, ?, ?, ?)", (artist, album, year, genre))
    #cur.execute("INSERT INTO albums VALUES (?, ?, ?, ?, ?)", (id, artist, album, year, genre))
    conn.commit() # tallentaa tiedon tietokantaan
    

def fetch_albums():
    cur.execute("SELECT * FROM albums")
    print(cur.arraysize)
    rows = cur.fetchall()
    result = []
    for row in rows:
        result.append(
            str(row[0])
            + "-"
            + str(row[1])
            + "-"
            + row[2]
            + "-"
            + row[3]
            + "-"
            + str(row[4])
        )
    return result


def remove(selected_album):
    cur.execute(
        "DELETE FROM albums WHERE id=?", (selected_album[0],)
    )  # needs comma, because is tuple
    conn.commit()


def update(selected_album, artist, album, year, genre):
    #print(id)
    cur.execute(
        "UPDATE albums SET artist_name = ?, album_name = ?, year = ?, genre = ? WHERE id = ?",
        (artist, album, year, genre, selected_album[0]),
    )
    conn.commit()


def get_max_id():
    cur.execute("SELECT MAX(id) from albums")    
    res = cur.fetchone()    
    if res[0] !=None:
        return res[0]
    else:
        return 0


def __del__():  # destructor call when all instances of object has been deleted
    print("__del__ called")
    conn.close()
