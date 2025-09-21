import sqlite3

with sqlite3.connect('my_database.db') as connection:

    cursor = connection.cursor()

    select_query = "SELECT * FROM Students;"


    cursor.execute(select_query)

    all_students = cursor.fetchmany(3)

    print("All Students:")
    for student in all_students:
        print(student)
