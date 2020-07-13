import sqlite3

db = sqlite3.connect('contacts.sqlite')
email = input('Please Enter your email ')
# for row in db.execute('SELECT * FROM sqlite_master'):

string_db = 'SELECT * FROM contacts WHERE email = ?'

for row in db.execute(string_db, (email,)):
    print(row)

db.close()

# Completed - 15. SQL Injection Attacks
