import sqlite3

import csv

con = sqlite3.connect("db.sqlite3")
cur = con.cursor()

with open('import_csv.txt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)
        try:
            cur.execute("INSERT INTO members_member (firstname, lastname, phone, joined_date) VALUES(?,?,?,?)", row)
        except sqlite3.Error as error: 
            print("Error inserting vale into table.")
print("Committing changes ...")
try:
    con.commit()
except sqlite3.Error as error:
    print("Error doing commit")

print("done. Closing database...")
try:
    con.close()
except sqlite3.Error as error:
    print("Error doing commit")

print("Done")