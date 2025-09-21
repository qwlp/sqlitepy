import sqlite3

with sqlite3.connect("my_database.db") as connection:
    cursor = connection.cursor()

    update_query = '''
        UPDATE Students
        SET age = ?
        WHERE name = ?;
    '''
    new_age = 21
    student_name = 'Jane Doe'

    cursor.execute(update_query, (new_age, student_name))

    connection.commit()
    
    print(f"Update {student_name} to {new_age}")
 
