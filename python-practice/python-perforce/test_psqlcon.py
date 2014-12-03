import psycopg2

# connect with database
conn = psycopg2.connect(database="cpm", user="mintan2", password="189441553", host="localhost", port="5432")
print ("Opened database successfully")

# instaniate
cur = conn.cursor()

# test creating table
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print ("Table created successfully")
conn.commit()

# test inserting data
n = 5
name = 'Waterloo'
n2 = 33
name2 = 'Ontario'
n3 = 111111.00
cur.execute("insert into company (id, name, age, address, salary) \
	values (%s, %s, %s, %s, %s)",(n, name, n2, name2, n3))
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
print ("Records created successfully")
conn.commit()

# test select queries
cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Select done successfully")

# test updating
cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
conn.commit
print ("Total number of rows updated :", cur.rowcount)

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Update done successfully")

# test deleting
cur.execute("DELETE from COMPANY where ID=2;")
conn.commit
print ("Total number of rows deleted :", cur.rowcount)

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("SALARY = ", row[3], "\n")
print ("Deleting done successfully")

cur.execute("SELECT id from COMPANY where age=32")
file_id = cur.fetchall()
for file in file_id:
	id = file[0]
	print (id)

cur.execute("select exists (select true from company where id = 2);")
bol = cur.fetchall()
print (bol)
for b in bol:
	id = b[0]
	print (id)

conn.close()
