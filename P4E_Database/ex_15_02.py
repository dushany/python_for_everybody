# read roster data in JSON format, parse the file, and
# produce a SQLite database
import json
import sqlite3

# database connection
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# database setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id INTEGER,
    course_id INTEGER,
    role INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

f_name = input('Enter file name: ')
if len(f_name) < 1:
    f_name = 'roster_data.json'

str_data = open(f_name).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    # update User table
    cur.execute('INSERT OR IGNORE INTO User(name) VALUES(?)',(name,))
    cur.execute('SELECT id FROM User WHERE name = ?',(name,))
    user_id = cur.fetchone()[0]

    # update Course table
    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES(?)',(title,))
    cur.execute('SELECT id FROM Course WHERE title = ?',(title,))
    course_id = cur.fetchone()[0]

    # update Member table
    cur.execute('''
    INSERT OR REPLACE INTO Member(user_id,course_id,role) VALUES(?,?,?)''',
    (user_id, course_id, role))

    conn.commit()
