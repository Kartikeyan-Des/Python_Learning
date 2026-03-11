import sqlite3

def init_db():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tblStudent(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Grade TEXT           
        )
    ''')
    conn.commit()
    return conn

def add_student(conn):
    Name = input("Enter your Name: ")
    Grade = input("Enter your Grade: ")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tblStudent (Name, Grade) VALUES (?, ?) ', (Name, Grade) )
    conn.commit()
    print(f"Added {Name} Successfully!....")

def view_student(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * from tblStudent")
    rows = cursor.fetchall()

    print("\n-- Student List --")
    for row in rows:
        print(f" ID:{row[0]}, Name:{row[1]}, Grade:{row[2]}")
    
db_connection = init_db()
add_student(db_connection)
view_student(db_connection)
db_connection.close()   