#programmer: Devin Goshaw
#date: 12/5/25
#program: phone book database 

import sqlite3

def create_phonebook_db():
    
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            PhoneNumber TEXT NOT NULL
        )
    ''')

    sample_entries = [
        ('Bob fred', '611-543-1234'),
        ('Bob Smith', '654-123-5678'),
        ('Bob Brown', '523-234-8765'),
        ('Bob Purple', '555-666-4321')
    ]

    cur.execute("SELECT COUNT(*) FROM Entries")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", sample_entries)
        print("Inserted sample entries into the phonebook database.")
    else:
        print("Entries table already has data. No rows added.")

    conn.commit()
    conn.close()
    print("Database 'phonebook.db' created and ready to use.")

create_phonebook_db()