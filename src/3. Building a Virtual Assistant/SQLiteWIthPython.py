import sqlite3

conn = sqlite3.connect('../../data/hotels.db')

c = conn.cursor()

c.execute("SELECT * FROM hotels")
c.fetchall()

c.execute("SELECT * FROM hotels WHERE area='south' and price='hi'")
c.fetchall()

# Bad Idea
# query = "SELECT name from restaurant where area='{}'".format(area)
# c.execute(query)

# Better
t = (area,price)
c.execute('SELECT * FROM hotels WHERE area=? and price=?', t)

