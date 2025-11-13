import sqlite3

# Connect with SQLite
connection = sqlite3.connect("student.db")
cursor = connection.cursor()

# Create table if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(25), 
    CLASS VARCHAR(25),
    SECTION VARCHAR(25), 
    MARKS INT
)
"""
cursor.execute(table_info)

# Insert records (optional: to avoid duplicates, you can use INSERT OR IGNORE)
records = [
    ('Piyush', 'Data Science', 'A', 90),
    ('Mukul', 'Maths', 'B', 86),
    ('Yogesh', 'Maths', 'A', 70),
    ('Chutkush', 'Data Science', 'B', 20),
    ('Chotu', 'Maths', 'A', 30),
    ('Lankesh', 'Data Science', 'B', 75)
]

cursor.executemany('INSERT INTO STUDENT VALUES (?, ?, ?, ?)', records)

# Display all records
print("The inserted records are:")
cursor.execute('SELECT * FROM STUDENT')
for row in cursor.fetchall():
    print(row)

# Commit and close
connection.commit()
connection.close()
