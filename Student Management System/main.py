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

def update_student(conn):
    student_id = input("Enter the student ID: ")

    new_name = input("Enter new Name: ")
    new_grade = input("Enter new Grade: ")

    cursor= conn.cursor()
    cursor.execute('''
        UPDATE tblStudent 
        SET Name = ?, Grade = ? 
        WHERE ID = ?
    ''', (new_name, new_grade, student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"Student ID {student_id} Updated Successfully!.... ")
    else:
        print(f"No Student Found for Student ID: {student_id}")


def search_students(conn):
    Name = input("Enter the Student Name: ")

    cursor = conn.cursor()
    cursor.execute('''
    SELECT * from tblStudent WHERE Name LIKE ?

''',(Name + '%',))
    
    rows = cursor.fetchall()

    if rows:
        print("\n-- Search Results --")
        for row in rows:
            print(f"ID:{row[0]}, Name:{row[1]}, Grade:{row[2]}")
    else:
        print(f"No student found with name '{Name}'")

    
    conn.commit()

def delete_students(conn):
    student_id = input("Enter ID to delete: ")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tblStudent WHERE ID = ?', (student_id,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Student ID {student_id} Deleted Successfully!.... ")
    else:
        print(f"No Student Found for Student ID: {student_id}")


db_connection = init_db()

while True:
    print("\n --Student Mangement System-- ")
    print("1. Add Students")
    print("2. View Students")
    print("3. Update Students")
    print("4. Search Student Lists")
    print("5. Delete Student")
    print("6. Exit ")

    choice = input("Enter your Choice: ")

    if choice == "1":
        add_student(db_connection)
    elif choice == "2":
        view_student(db_connection)
    elif choice == "3":
        update_student(db_connection)
    elif choice == "4":
        search_students(db_connection)
    elif choice == "5":
        delete_students(db_connection)
    elif choice == "6":
        db_connection.close() 
        break 
    else:
        print("Invalid Choice, Try Again...")


  