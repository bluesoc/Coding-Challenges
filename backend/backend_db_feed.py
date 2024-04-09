'''
	Python Script Created to populate
	a database with data from a file

	bluesoc (c) 2024

'''
#!/usr/bin/env python
import sqlite3

table = "book_outlet_book"

# Cols= id, title, rating, author, is_bestselling

# Starting primary-key
pk = 9

filename = "db.sqlite3"

con = sqlite3.connect(filename)
cur = con.cursor()


# Fetch data from file
data = []

booklist = open("dump").readlines()
for book in booklist:
	best = [0]

	temp = []
	temp.insert(0, pk)
	bookstrip = book.strip().split(";")

	try:
		if float(bookstrip[1]) >= 4.60:
			best = [1]
	except Exception as err:
		print(err)
		continue

	temp = temp + bookstrip + best + ['']

	data.append(temp)
	pk += 1

print(data)

res = cur.executemany("INSERT INTO book_outlet_book VALUES(?, ?, ?, ?, ?, ?)", data)
con.commit()
print(res.fetchone())
