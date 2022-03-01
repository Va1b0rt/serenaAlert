import sqlite3

conn = sqlite3.connect("messages.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def create_table():

    cursor.execute("""CREATE TABLE IF NOT EXISTS message
                    (time text, message text, message_id text)
                """)


def insert_message(time, message, message_id):
    cursor.execute(f"""INSERT INTO message
                      VALUES ('{time}', '{message}', '{message_id}')"""
                   )

    conn.commit()


def update_message(message_id_last, message_id_new, time, message):
    sql = f"""
    UPDATE message 
    SET time = '{time}',  message = '{message}', message_id = '{message_id_new}'
    WHERE message_id = '{message_id_last}'
    """

    cursor.execute(sql)
    conn.commit()


def select_message():
    sql = "SELECT * FROM message"
    cursor.execute(sql)
    return cursor.fetchall()


if __name__ == '__main__':
    create_table()
    insert_message('123', 'HelloWorld!!!', '1')
    print(select_message())
    update_message(select_message()[0][2], '321', 'qwerty', '2')
    print(select_message())



