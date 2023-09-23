"""
Здесь реализована взаимодействие с sqlite3 базой данных (users.db)
"""

import sqlite3
import threading


# Ищем пользователя в базе данных (для функции "показать профиль")
def find_user_by_chat_id(chat_id, db):

    query = f"SELECT * FROM users WHERE chat_id = {chat_id}"

    cursor = db.execute_query(query)
    record = cursor.fetchone()

    if record:
        user_id, chat_id, name, surname, email, age, type_diabetes, city, number, access = record
        return {
            "user_id": user_id,
            "chat_id": chat_id,
            "Имя": name,
            "Фамилия": surname,
            "Почта": email,
            "Возраст": age,
            "Тип диабета": type_diabetes,
            "Город": city,
            "Номер телефона": number,
            "access": access
        }
    else:
        return None


def connect_db():

    # Создание объекта базы данных
    db = Database()
    # Установка соединения с базой данных
    db.connect()
    # Создание таблиц, если они не существует
    db.create_tables()

    return db


class Database:

    def __init__(self):
        self.db_file = "users.db"
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
        return cursor

    def create_tables(self):
        users_table_query = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT,
                name TEXT,
                surname TEXT,
                email TEXT,
                age TEXT,
                type_diabetes TEXT,
                city TEXT,
                number TEXT,
                access INTEGER
            )
            '''
        testing_table_query = '''
            CREATE TABLE IF NOT EXISTS testing (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id TEXT,
                question_1 TEXT,
                question_2 TEXT,
                question_3 TEXT
            )
        '''
        self.execute_query(users_table_query)
        self.execute_query(testing_table_query)

    def get_all_users(self):
        query = "SELECT * FROM users"
        cursor = self.connect().cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def get_all_answers(self):
        query = "SELECT * FROM testing"
        cursor = self.connect().cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        return records

    def delete_user(self, user_id):
        query = f'DELETE FROM users WHERE chat_id = ?'
        self.execute_query(query, [str(user_id)])

    def clear_users_table(self):
        query = 'DELETE FROM users'
        self.execute_query(query)

    def clear_testing_table(self):
        query = 'DELETE FROM testing'
        self.execute_query(query)

    def add_user(self, chat_id, name, surname, email,
                 age=None, type_diabetes=None, city=None,
                 number=None, access=None):
        query = 'INSERT INTO users (chat_id, name, surname, email'
        params = [chat_id, name, surname, email]
        value = "VALUES (?, ?, ?, ?"

        if all((age, type_diabetes, city, number, access)):
            query += ', age, type_diabetes, city, number, access'
            value += ', ?, ?, ?, ?, ?'
            params.append([age, type_diabetes, city, number, access])

        query += ') ' + value + ')'

        self.execute_query(query, tuple(params))

    def update_user(self, chat_id, user_data):
        query = 'UPDATE users SET ' \
                'name = ?, surname = ?, email = ?, age = ?, type_diabetes = ?, city = ?, number = ?, access = ? ' \
                'WHERE chat_id = ?'

        params = (user_data["name"],
                  user_data["surname"],
                  user_data["email"],
                  user_data["age"],
                  user_data["type_diabetes"],
                  user_data["city"],
                  user_data["number"],
                  user_data["access"],
                  chat_id
                  )

        self.execute_query(query, params)

    def insert_user_answers(self, results):
        query = 'INSERT INTO testing (chat_id, question_1, question_2, question_3) VALUES (?, ?, ?, ?)'
        self.execute_query(query, results)
