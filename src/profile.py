from telebot import types
from src.keyboards import main_menu_kb
from src.database import find_user_by_chat_id
from main import logger as logger


def show_profile(message, db, bot):

    logger.info(f"User {message.chat.id} has asked to show him his profile")

    result = find_user_by_chat_id(message.chat.id, db)

    if result:
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


def edit_profile_questionnaire(message, user_data, db, bot):
    chat_id = message.chat.id

    # Запрашиваем возраст
    bot.send_message(chat_id, 'Введите ваш возраст:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_age(message, user_data, db, bot))


def edit_profile(message, db, bot):

    logger.info(f"User {message.chat.id} has started to edit his profile")

    chat_id = message.chat.id
    user_data = {}
    bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_name(message, user_data, db, bot))


def edit_name(message, user_data, db, bot):
    chat_id = message.chat.id
    name = message.text

    # Сохраняем имя
    user_data['name'] = name

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: edit_surname(message, user_data, db, bot))


def edit_surname(message, user_data, db, bot):
    chat_id = message.chat.id
    surname = message.text

    # Сохраняем фамилию
    user_data['surname'] = surname

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda message: edit_email(message, user_data, db, bot))


def edit_email(message, user_data, db, bot):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    user_data['email'] = email

    # Запрашиваем возраст
    bot.send_message(chat_id, 'Введите ваш возраст:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_age(message, user_data, db, bot))


def edit_age(message, user_data, db, bot):
    chat_id = message.chat.id
    age = message.text

    # Сохраняем возраст
    user_data['age'] = age

    # Запрашиваем тип диабета
    bot.send_message(chat_id, 'Выберете ваш тип диабета:')
    bot.register_next_step_handler(message, lambda message: edit_type_diabetes(message, user_data, db, bot))


def edit_type_diabetes(message, user_data, db, bot):
    chat_id = message.chat.id
    type_diabetes = message.text

    # Сохраняем тип диабета
    user_data['type_diabetes'] = type_diabetes

    # Запрашиваем город
    bot.send_message(chat_id, 'Введите ваш город:', reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, lambda message: edit_place(message, user_data, db, bot))


def edit_place(message, user_data, db, bot):
    chat_id = message.chat.id
    city = message.text

    # Сохраняем город
    user_data['city'] = city

    # Запрашиваем контактный номер
    bot.send_message(chat_id, 'Введите ваш контактный номер:')
    bot.register_next_step_handler(message, lambda message: edit_number(message, user_data, db, bot))


def edit_number(message, user_data, db, bot):
    chat_id = message.chat.id
    number = message.text

    # Сохраняем контактный телефон
    user_data['number'] = number
    # Добавляем флаг "анкетирование пройдено"
    user_data['access'] = 1

    # Обновляем инфо в базе данных
    db.update_user(chat_id, user_data)

    # Завершаем редактирование и отправляем клавиатуру с главным меню
    bot.send_message(chat_id, 'Данные сохранены', reply_markup=main_menu_kb(message, types.ReplyKeyboardMarkup(resize_keyboard=True), db))
    logger.info(f"User {message.chat.id} has finished to fill questionnaire")
