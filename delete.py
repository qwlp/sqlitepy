import sqlite3

with sqlite3.connect('my_database.db') as connection:
    cursor = connection.cursor()

    delete_query = '''
        DELETE FROM Students
        WHERE name = ?
    '''

    student_name = 'Jane Doe'

    cursor.execute(delete_query, (student_name,))

    connection.commit()

    print(f"Deleted {student_name}")
    
