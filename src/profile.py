from telebot import types
from src.keyboards import main_menu_kb
from src.users import connect_db, find_user_by_chat_id


def show_profile(message, bot):
    result = find_user_by_chat_id(message.chat.id)

    profile = f"""
Имя: {result["Имя"]}
Фамилия: {result["Фамилия"]}
Почта: {result["Почта"]}
Возраст: {result["Возраст"]}
Тип диабета: {result["Тип диабета"]}
Город: {result["Город"]}
Номер телефона: {result["Номер телефона"]}
    """

    bot.send_message(message.chat.id, profile)

def edit_profile_questionnaire(message, bot):
    chat_id = message.chat.id
    db = connect_db("users.db")
    users = {chat_id: {}}
    bot.send_message(message.chat.id, 'Сколько вам лет?', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_age(message, users, db, bot))


def edit_profile(message, bot):
    chat_id = message.chat.id
    db = connect_db("users.db")
    users = {chat_id: {}}
    bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_name(message, users, db, bot))


def edit_name(message, users, db, bot):
    # Сохраняем имя
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: edit_surname(message, users, db, bot))


def edit_surname(message, users, db, bot):
    # Добавляем фамилию
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda message: edit_email(message, users, db, bot))


def edit_email(message, users, db, bot):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    users[chat_id]['email'] = email
    user_info = users[chat_id]
    db.update_partial_user(chat_id, name=user_info['name'], surname=user_info['surname'], email=user_info['email'])
    bot.send_message(chat_id, 'Введите ваш возраст:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_age(message, users, db, bot))


def edit_age(message, users, db, bot):
    chat_id = message.chat.id
    age = message.text
    users[chat_id]['age'] = age

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("1"), types.KeyboardButton("2"))
    bot.send_message(chat_id, 'Выберете ваш тип диабета:', reply_markup=markup)
    bot.register_next_step_handler(message, lambda message: edit_type_diabetes(message, users, db, bot))


def edit_type_diabetes(message, users, db, bot):
    chat_id = message.chat.id
    type_diabetes = message.text
    users[chat_id]['type_diabetes'] = type_diabetes
    bot.send_message(chat_id, 'Введите ваш город:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_place(message, users, db, bot))


def edit_place(message, users, db, bot):
    chat_id = message.chat.id
    place = message.text
    users[chat_id]['place'] = place
    bot.send_message(chat_id, 'Введите ваш контактный номер:')
    bot.register_next_step_handler(message, lambda message: edit_number(message, users, db, bot))


def edit_number(message, users, db, bot):
    chat_id = message.chat.id
    number = message.text
    users[chat_id]['number'] = number
    users[chat_id]['access'] = 1
    user_info = users[chat_id]
    db.update_partial_user(chat_id, age=user_info['age'], type_diabetes=user_info['type_diabetes'], place=user_info['place'], number=user_info['number'], access=user_info['access'])
    bot.send_message(chat_id, 'Данные сохранены')
    main_menu_kb(message, types.ReplyKeyboardMarkup(resize_keyboard=True), bot)

