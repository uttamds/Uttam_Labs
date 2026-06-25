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
