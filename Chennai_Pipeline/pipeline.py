import sqlite3

def init_db():
    conn = sqlite3.connect("chennai_data.db")
    cursor = conn.cursor()
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS tblWeather(
                   ID INTEGER Primary key AUTOINCREMENT,
                   City Text,
                   Temperature Real,
                   Feels_Like Real,
                   Humidity INTEGER,
                   Weather Text,
                   Timestamp TEXT
                   )
    ''')
    conn.commit()
    return conn