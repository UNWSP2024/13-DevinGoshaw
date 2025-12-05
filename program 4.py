#Programmer: Devin Goshaw
#date: 12/5/25
#program: phonebook database display 


import sqlite3

DB_NAME = "phonebook.db"

def view_entries():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT EntryID, Name, PhoneNumber FROM Entries")
    rows = cur.fetchall()
    conn.close()

    if rows:
        print("\nPhone Book Entries:")
        print("------------------")
        for entry_id, name, phone in rows:
            print(f"{entry_id}: {name} - {phone}")
    else:
        print("\nNo entries found.")

def add_entry():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
    conn.commit()
    conn.close()
    print(f"Added {name} to phone book.")

def update_entry():
    view_entries()
    entry_id = input("Enter the EntryID of the contact to update: ")
    new_phone = input("Enter the new phone number: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE Entries SET PhoneNumber = ? WHERE EntryID = ?", (new_phone, entry_id))
    conn.commit()
    conn.close()
    print("Phone number updated.")

def delete_entry():
    view_entries()
    entry_id = input("Enter the EntryID of the contact to delete: ")
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM Entries WHERE EntryID = ?", (entry_id,))
    conn.commit()
    conn.close()
    print("Entry deleted.")

def main():
    while True:
        print("\nPhone Book Menu")
        print("1. View all entries")
        print("2. Add a new entry")
        print("3. Update a phone number")
        print("4. Delete an entry")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_entries()
        elif choice == "2":
            add_entry()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()