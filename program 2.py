#programmer: Devin Goshaw
#Date: 12/5/25
#program: display cities database 

import sqlite3

def display_cities():
    
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    cur.execute("SELECT CityName, Population FROM Cities")
    cities = cur.fetchall()

    print("Cities in the database:")
    print("------------------------")
    for city, population in cities:
        print(f"{city}: {population}")

    conn.close()

if __name__ == "__main__":
    display_cities()