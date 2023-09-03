import sqlite3
import threading


def connect_db(path_db):
    db = Database(path_db)
    # Установка соединения с базой данных
    db.connect()
    # Создание таблицы, если она не существует
    db.create_table()

    return db


class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self._connection = threading.local()

    def connect(self):
        conn = getattr(self._connection, 'conn', None)
        if conn is None:
            conn = sqlite3.connect(self.db_file)
            self._connection.conn = conn
        return conn

    def __del__(self):
        conn = getattr(self._connection, 'conn', None)
        if conn is not None:
            conn.close()

    def execute_query(self, query, params=None):
        conn = self.connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        return cursor.lastrowid

    def create_table(self):
        query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                email TEXT
            )
        '''
        self.execute_query(query)

    def insert_user(self, name, surname, email):
        query = f"INSERT INTO users (name, surname, email) " \
                f"VALUES ({name}, {surname}, {email})"
        self.execute_query(query)

    def get_all_records(self):
        query = "SELECT * FROM users"
        cursor = self.connect().cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def delete_user(self, user_id):
        query = f'DELETE FROM users WHERE id = {user_id}'
        self.execute_query(query)

    def clear_database(self):
        query = 'DELETE FROM users'
        self.execute_query(query)
