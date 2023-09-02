from users import Database, connect_db
from telebot import types

def questionnaire(message, bot):
    if message.text == "Да":
        pass
    elif message.text == "Нет":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_education = types.KeyboardButton("Пройти обучение")
        btn_profile = types.KeyboardButton("Профиль")
        btn_social_media = types.KeyboardButton('Об онлайн-школе')
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_education, btn_profile, btn_social_media, btn_main_menu)
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)
    else:
        bot.register_next_step_handler(message, lambda messege: questionnaire(messege, bot))


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

    # Сохраняем информацию в базу данных
    db.insert_user(user_info['name'], user_info['surname'], user_info['email'])

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_yes = types.KeyboardButton('Да')
    btn_no = types.KeyboardButton('Нет')
    markup.add(btn_yes, btn_no)
    bot.send_message(chat_id, 'Для составления персональной программы обучения нам нужно задать вам несколько вопросов. Хотите заполнить анкету сейчас?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda messege: questionnaire(messege, bot))
