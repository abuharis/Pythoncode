import sqlite3

connect = sqlite3.connect("C:\\Users\\abuharis.salih\\Documents\\database\\publish.db")

cur = connect.cursor()

#create Table
cur.execute('''CREATE TABLE IF NOT EXISTS posts  (id int, date text, title text, content text, public integer)''')

#Insert items into a the table
cur.execute("INSERT INTO posts VALUES (1, '2024-01-24', 'First blog', 'Favorite blog', 1)")
cur.execute("INSERT INTO posts VALUES (2, '2024-01-24', 'Secret blog', 'Secure this from someone', 0)")

# cur.execute("SELECT * FROM blogs where id='first-blog'")
# result = cur.fetchall()
# print(result[0][0])

#Save changes
connect.commit()


#Close connection
connect.close()