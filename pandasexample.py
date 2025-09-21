import sqlite3
import pandas as pd

with sqlite3.connect("my_database.db") as connection:

    select_query = "SELECT * FROM Students;"

    df = pd.read_sql(select_query, connection)

print(df)
