import sqlite3

kapcsolat = sqlite3.connect('minta.db')

ab =kapcsolat.cursor()

ab.execute('CREATE TABLE IF NOT EXISTS emberek (nev TEXT, kor INTEGER)')
nev = 'Julcsi'
kor = 25
ab.execute('INSERT INTO emberek VALUES(?, ?)', (nev, kor))

kapcsolat.close()