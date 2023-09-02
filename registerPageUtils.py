import telebot
from users import Database
from startDobra import bot

def connect_db(path_db):
    db = Database(path_db)
    # Установка соединения с базой данных
    db.connect()
    # Создание таблицы, если она не существует
    db.create_table()

    return db

@bot.message_handler(commands=['clear_db'])
def clear_db(messege):
    db = connect_db("users.db")
    db.clear_database()

@bot.message_handler(commands=['delete_user'])
def delete_user(messege):
    db = connect_db("users.db")
    bot.send_message(messege.chat.id, 'Введите id пользователя, которого нужно удалить:')
    db.clear_database()
@bot.message_handler(commands=['all'])
def view_all(messege):
    db = connect_db("users.db")
    all_records = db.get_all_records()
    bot.send_message(messege.chat.id, "id | name | surname | email")
    for record in all_records:
        bot.send_message(messege.chat.id, f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")
@bot.message_handler(commands=['register'])
def handle_register(message):
    chat_id = message.chat.id
    users = {}
    db = connect_db("users.db")
    # Запрашиваем имя
    bot.send_message(chat_id, 'Введите ваше имя:')
    bot.register_next_step_handler(message, lambda messege: process_name_step(messege, users, db))

def process_name_step(message, users, db):
    chat_id = message.chat.id
    name = message.text

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda messege: process_surname_step(messege, users, db))

    # Сохраняем имя
    users[chat_id] = {'name': name}

def process_surname_step(message, users, db):
    chat_id = message.chat.id
    surname = message.text

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda messege: process_email_step(messege, users, db))

    # Добавляем фамилию
    users[chat_id]['surname'] = surname

def process_email_step(message, users, db):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    users[chat_id]['email'] = email

    # Выводим информацию о пользователе
    user_info = users[chat_id]
    info_message = f'Имя: {user_info["name"]}\nФамилия: {user_info["surname"]}\nПочта: {user_info["email"]}'
    bot.send_message(chat_id, info_message)

    # Сохраняем информацию в базу данных
    db.insert_user(user_info['name'], user_info['surname'], user_info['email'])
bot.polling(none_stop=True, interval=0)