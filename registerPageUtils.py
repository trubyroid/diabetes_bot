from users import Database, connect_db

def process_name_step(message, users, db, bot):
    chat_id = message.chat.id
    name = message.text

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda messege: process_surname_step(messege, users, db, bot))

    # Сохраняем имя
    users[chat_id] = {'name': name}

def process_surname_step(message, users, db, bot):
    chat_id = message.chat.id
    surname = message.text

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda messege: process_email_step(messege, users, db, bot))

    # Добавляем фамилию
    users[chat_id]['surname'] = surname

def process_email_step(message, users, db, bot):
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