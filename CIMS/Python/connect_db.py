import sqlite3

# 1. connect to database
con = sqlite3.connect("college.db")
cur = con.cursor()

# 2. create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")

# 3. insert record
cur.execute("INSERT INTO student VALUES (101, 'Aarav', 'Python', 82)")

# 4. commit changes
con.commit()

# 5. fetch records
cur.execute("SELECT * FROM student")
rows = cur.fetchall()

print("Student Records:")
for row in rows:
    print(row)

# 6. close connection
con.close()

====================
Verson 2
====================

import sqlite3

# connect to database
con = sqlite3.connect("college.db")
cur = con.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    course TEXT,
    marks INTEGER
)
""")

while True:
    print("\n===== STUDENT DATABASE MENU =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course Name: ")
        marks = int(input("Enter Marks: "))

        cur.execute(
            "INSERT INTO student VALUES (?, ?, ?, ?)",
            (student_id, name, course, marks)
        )
        con.commit()
        print("Student record inserted successfully.")

    elif choice == "2":
        cur.execute("SELECT * FROM student")
        rows = cur.fetchall()

        print("\nStudent Records:")
        if len(rows) == 0:
            print("No records found.")
        else:
            for row in rows:
                print(row)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")

con.close()
