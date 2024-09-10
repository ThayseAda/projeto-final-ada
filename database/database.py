import sqlite3

conn =  sqlite3.connect('PetData.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Pets(
                  Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                  Especie TEXT(150) NOT NULL,
                  Idade INTEGER NOT NULL,
                  Peso REAL NOT NULL,
                  Data DATETIME NOT NULL,
                  Historico TEXT(800)
               );
               """) 
conn.commit()