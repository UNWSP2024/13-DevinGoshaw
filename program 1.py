#Devin Goshaw 
#Date: 12/5/25
#program: cities database

import sqlite3

def create_cities_db():
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Cities (
            CityID INTEGER PRIMARY KEY AUTOINCREMENT,
            CityName TEXT,
            Population REAL
        )
    ''')

    cities = [
        ('Tokyo',38001000), ('Delhi',25703168), ('Shanghai',23740778),
        ('Sao Paulo',21066245), ('Mumbai',21042538), ('Mexico City',20998543),
        ('Beijing',20383994), ('Osaka',20237645), ('Cairo',18771769),
        ('New York',18593220), ('Dhaka',17598228), ('Karachi',16617644),
        ('Buenos Aires',15180176), ('Kolkata',14864919), ('Istanbul',14163989),
        ('Chongqing',13331579), ('Lagos',13122829), ('Manila',12946263),
        ('Rio de Janeiro',12902306), ('Guangzhou',12458130)
    ]

    cur.execute("SELECT COUNT(*) FROM Cities")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Cities (CityName, Population) VALUES (?, ?)", cities)
        print("Inserted 20 cities into the database.")
    else:
        print("Cities table already has data. No rows added.")

    conn.commit()
    conn.close()
    print("Database 'cities.db' created")

create_cities_db()