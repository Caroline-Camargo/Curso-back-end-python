import sqlite3 as sql

conection = sql.connect('database') # Connect to the database
cursor = conection.cursor() # Create a cursor object to interact with the database

#cursor.execute('CREATE TABLE users(id INT, name VARCHAR(100), adress VARCHAR(100), email VARCHAR(100));') # Execute a sql command
#cursor.execute('CREATE TABLE maneger(id INT, name VARCHAR(100), adress VARCHAR(100), email VARCHAR(100));') # Execute a sql command
#cursor.execute('CREATE TABLE product(id INT, name VARCHAR(100), adress VARCHAR(100), email VARCHAR(100));') 

#cursor.execute('ALTER TABLE users RENAME TO user')
#cursor.execute('ALTER TABLE user ADD COLUMN telphone INT')
#cursor.execute('ALTER TABLE user RENAME COLUMN telphone TO telephone') 

#cursor.execute('DROP TABLE product') 

#cursor.execute('INSERT INTO user(id, name, adress, email, telephone) VALUES(1, "Caroline", "Pelotas", "carol@gmail.com", 123456)')
#cursor.execute('INSERT INTO user(id, name, adress, email, telephone) VALUES(2, "Yasmin", "Pelotas", "yasmin@gmail.com", 123456)')
#cursor.execute('INSERT INTO user(id, name, adress, email, telephone) VALUES(3, "Elizabeth", "Tapes", "elizabeth@gmail.com", 123456)')
#cursor.execute('INSERT INTO user(id, name, adress, email, telephone) VALUES(4, "Osmar", "Araça", "osmar@gmail.com", 123456)')
#cursor.execute('INSERT INTO manager(id, name, adress, email) VALUES(2, "Yasmin", "Pelotas", "carol@gmail.com")')
#cursor.execute('INSERT INTO manager(id, name, adress, email) VALUES(3, "Joao", "Sao Paulo", "joao@gmail.com")')
#cursor.execute('INSERT INTO manager(id, name, adress, email) VALUES(33, "Cintia", "Rio", "cintia@gmail.com")')


#cursor.execute('DELETE FROM user WHERE id = 1')
#cursor.execute('UPDATE user SET adress = "Minas Gerais" WHERE name = "Osmar"')

#ORDER BY and DESC
#data = cursor.execute('SELECT * FROM user ORDER BY name DESC') # Select all users from the table user

# LIMIT is used to limit the number of rows returned 
# DISTINCT is used to return only distinct values
#data = cursor.execute('SELECT DISTINCT * FROM user LIMIT 2')

# GROUP BY is used to group rows that have the same values
# HAVING is used to filter the rows that a GROUP BY returns
#data = cursor.execute('SELECT name FROM user GROUP BY name HAVING id > 2')

# JOIN is used to combine rows from two or more tables, based on a related column between them
# INNER JOIN is used to return rows when there is at least one match in both tables
# data = cursor.execute('SELECT * FROM user INNER JOIN manager ON user.id = manager.id')

# LEFT JOIN is used to return all rows from the left table, and the matched rows from the right table
#data = cursor.execute('SELECT * FROM user LEFT JOIN manager ON user.name = manager.name')


# RIGHT JOIN is used to return all rows from the right table, and the matched rows from the left table
# data = cursor.execute('SELECT * FROM user RIGHT JOIN manager ON user.name = manager.name')

# FULL JOIN is used to return rows when there is a match in one of the tables
# data = cursor.execute('SELECT * FROM user FULL JOIN manager ON user.name = manager.name')

# SUBQUERIES are queries that are nested inside another query
data = cursor.execute('SELECT * FROM user WHERE name IN (SELECT name from manager)')

for user in data:
    print(user)

conection.commit() # Save the changes
conection.close()  # Close the connection