from database import conn, cursor

def get_tasks():
    cursor.execute("SELECT * FROM TASKS")
    rows=cursor.fetchall()

    return [
        {
            "id ": row[0],
            "title ": row[1],
            "done" :row[2]
        } for row in rows
    ]

def get_task(task_id):
    cursor.execute("SELECT * FROM TASKS WHERE ID = %s",(task_id,))
    row= cursor.fetchone()

    if row is None:
        return None

    return {
            "id" : row[0],
            "title" : row[1],
            "done" :row[2]
    }

def create_task(title):
    cursor.execute("INSERT INTO TASKS(TITLE,DONE) VALUES(%s,%s)",(title,False))
    conn.commit()

    return cursor.lastrowid


def update_task(task_id,title,done):

    cursor.execute("""UPDATE TASKS SET TITLE=%s , DONE=%s WHERE ID=%s""",(title,done,task_id))
    conn.commit()

    return cursor.rowcount

def delete_task(task_id):
    cursor.execute("DELETE FROM TASKS WHERE ID = %s",(task_id,))
    conn.commit()

    return cursor.rowcount