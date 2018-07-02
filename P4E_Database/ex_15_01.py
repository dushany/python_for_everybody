# Musical Track Database
# read an iTunes export file in XML and produce a properly normalized database
import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

# Create intial tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# file input prompt
f_name = input('Enter file name: ')
if(len(f_name) < 1): f_name = 'Library.xml'

# XML lookup function
def lookup(d, key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None

content = ET.parse(f_name)
recs = content.findall('dict/dict/dict')

# loop through records
for entry in recs:
    if(lookup(entry,'Track ID') is None): continue

    artist = lookup(entry,'Artist')
    genre = lookup(entry,'Genre')
    album = lookup(entry,'Album')
    track = lookup(entry,'Name')
    length = lookup(entry,'Total Time')
    rating = lookup(entry,'Rating')
    play_count = lookup(entry,'Play Count')

    if artist is None or genre is None or album is None or track is None:
        continue

    # insert artist record
    cur.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ?',(artist,))
    artist_id = cur.fetchone()[0]

    # insert genre record
    cur.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ?',(genre,))
    genre_id = cur.fetchone()[0]

    # insert album record
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]

    # insert track record
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        (track, album_id, genre_id, length, rating, play_count))

    conn.commit()
