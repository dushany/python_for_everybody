# open file and count instances of email addresses. read
# email and count into Db file

import sqlite3

# # create DB and connection
conn = sqlite3.connect('my_email_DB.sqlite')
cur = conn.cursor()

# # create table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

# select and open text file
f_name = input("Enter file name:")
if(len(f_name)<1):
    f_name = 'mbox.txt'
f_head = open(f_name)

for line in f_head:
    if not line.startswith('From '):
        continue
    chnks = line.split()
    email = chnks[1]
    org = email.split('@')[1]
    cur.execute('SELECT count FROM Counts WHERE org = ?',(org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org,count) VALUES(?,1)', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
conn.commit()
