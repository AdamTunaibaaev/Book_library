import sqlite3
connection = sqlite3.connect('BookLibrary/database.db')
cursor = connection.cursor()
User_choise = input("Menu: \n1.Add Book \n2.Delete Book \n3.See my books \n")
if User_choise == '1':
  a=input("Name: ")
  b=input("Author: ")
  c=input("Year: ")
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS Books (
  id INTEGER PRIMARY KEY,
  Name TEXT NOT NULL,
  Author TEXT NOT NULL,
  Year INTEGER
  )
  ''')
  cursor.execute('INSERT INTO Books (Name, Author, Year) VALUES (?, ?, ?)', (a, b, c))
  connection.commit()
elif User_choise == '2':
  cursor.execute('SELECT * FROM Books')
  all_Books = cursor.fetchall()
  print(all_Books)
  abc=input("Book number: ")
  cursor.execute('DELETE FROM Books WHERE id = ?', (abc))
  connection.commit()
elif User_choise == '3':
  cursor.execute('SELECT * FROM Books')
  all_Books = cursor.fetchall()
  print(all_Books)
connection.close()

