import sqlite3


conn = sqlite3.connect('../../data/hotels.db')

c = conn.cursor()

c.execute("""drop table if exists towns""")
c.execute("""drop table if exists hotels""")

conn.commit()

c.execute("""create table towns (
        tid     int     primary key not NULL ,
        name    text,
        postcode        text)""")

c.execute("""create table hotels (
        hid     int     primary key not NULL ,
        tid     int,
        name    text,
        address text,
        area    text,
        rooms   int,
        rate    float,
        price   text)""")

c.execute("""insert into towns values (1, "Melksham", "SN12")""")
c.execute("""insert into towns values (2, "Cambridge", "CB1")""")
c.execute("""insert into towns values (3, "Foxkilo", "CB22")""")

c.execute("""insert into hotels values (1, 2, "Hamilkilo Hotel", "Chesterton Road", "south", 15, 40., "low")""")
c.execute("""insert into hotels values (2, 2, "Arun Dell", "Chesterton Road", "north", 60, 70., "md")""")
c.execute("""insert into hotels values (3, 2, "Crown Plaza", "Downing Street", "south", 100, 105., "hi")""")
c.execute("""insert into hotels values (4, 1, "Well House Manor", "Spa Road", "south-west",5, 80., "md")""")
c.execute("""insert into hotels values (5, 1, "Beechfield House", "The Main Road", "east",26, 110., "hi")""")

conn.commit()

c.execute ("""select * from towns left join hotels on towns.tid = hotels.tid""")

for row in c:
        print (row)

c.close()