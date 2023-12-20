import sqlite3

def create_table_if_not_exists(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            UserId INTEGER PRIMARY KEY AUTOINCREMENT,
            Username TEXT,
            Email TEXT,
            Password TEXT,
            PhoneNumber TEXT,
            Age INTEGER,
            Location TEXT,
            Gender TEXT,
            Image BLOB
        )
    ''')
    # ... (commit and close connection)

def store_user_data(cursor, conn, username, email, password, age, phonenumber, location, gender, image_path):
    cursor.execute(
        '''
        INSERT INTO Users(Username, Email, Password, PhoneNumber, Age, Location, Gender, Image)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
        ''', (username, email, password, phonenumber, age, location, gender, image_path)
    )
    # ... (commit and close connection)

# ... (other database functions)
