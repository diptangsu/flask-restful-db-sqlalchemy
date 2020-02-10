import sqlite3

with sqlite3.connect('data.db') as conn:
    cursor = conn.cursor()

    create_users_table = '''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )
    '''
    cursor.execute(create_users_table)
    conn.commit()
