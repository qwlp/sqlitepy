import sqlite3
from faker import Faker

fake = Faker(['en_IN'])
with sqlite3.connect('my_database.db') as connection:

    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER, 
        email TEXT
    );
    '''

    insert_query = '''
        INSERT INTO Students (name, age, email)
        VALUES (?,?,?);
    '''
    students_data = [(fake.name(), fake.random_int(min=18, max=25), fake.email()) for _ in range(5)]
    cursor.executemany(insert_query, students_data)

    connection.commit()
    
    print("Fake record inserted successfully!")



