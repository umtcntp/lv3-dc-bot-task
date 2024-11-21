import sqlite3

def connect_db():
    #The returned Connection object db_connection represents the connection to the on-disk database.
    db_connection = sqlite3.connect("taskDB.db")
    return db_connection

def create_table():
    #In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. 
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            _id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            complete BOOLEAN NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def add_task_to_db(task_description):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        INSERT INTO tasks(task, complete)
        VALUES(?, ?)
    ''', (task_description, 0))

    conn.commit()
    conn.close()

def delete_task_from_db(task_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        DELETE FROM tasks
        WHERE _id = ?
    ''', (task_id,))
    
    conn.commit()

    if cur.rowcount > 0:
        conn.close()
        return True
    else:
        conn.close()
        return False

def list_tasks():
    conn = connect_db()
    cur = conn.cursor()
    
    cur.execute('SELECT _id, task, complete FROM tasks')
    rows = cur.fetchall()
    conn.close()
    return rows    

def mark_task_complete(task_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        UPDATE tasks
        SET complete = 1
        WHERE _id = ?
    ''', (task_id,))

    conn.commit()

    if cur.rowcount > 0:
        conn.close()
        return True  
    else:
        conn.close()
        return False