# LUO VENV-VIRTAALIYMPÄRISTÖ
# JA AKTIVOI SE
# python -m venv env
# env\scripts\activate

import sqlite3 # asentuu pythonin mukana
from sqlite3 import Error

try:                      ## kokeile ../ niin saat virheen
    conn = sqlite3.connect("./databases/movies.db")
except Error as e:
    print(e) # mikä tahansa virhe tuleekin, tulostetaan se
