import sqlite3

connect = sqlite3.connect('bobri.sqlite')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Bobri(
id INTEGER PRIMARY KEY,
name TEXT,
view TEXT
)
''')

cursor.execute('''
DELETE FROM Bobri WHERE view = 'water'
 ''')

connect.commit()

result = cursor.execute('''
SELECT * FROM Bobri
''')

for i in result.fetchall():
    print(i)

connect.close()