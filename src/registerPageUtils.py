"""
В этом модуле реализована регистрация и запрос на прохождение анкетирования
"""

from src.keyboards import main_menu_kb, yes_or_no_kb
from src.profile import edit_profile_questionnaire
from main import logger as logger
from telebot import types
import messages


def process_name_step(message, user_data, db, bot):
    chat_id = message.chat.id
    name = message.text

    # Сохраняем имя
    user_data['name'] = name

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: process_surname_step(message, user_data, db, bot))


def process_surname_step(message, user_data, db, bot):
    chat_id = message.chat.id
    surname = message.text

    # Сохраняем фамилию
    user_data['surname'] = surname

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda message: process_email_step(message, user_data, db, bot))


def process_email_step(message, user_data, db, bot):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    user_data['email'] = email

    # Добавляем в базу данных информацию о новом пользователе
    db.add_user(chat_id, user_data['name'], user_data['surname'], user_data['email'])

    logger.info(f"User {message.chat.id} has finished registration")

    # Запрашиваем будет ли пользователь заполнять анкету
    bot.send_message(chat_id, messages.questionnaire_request, reply_markup=yes_or_no_kb(types.ReplyKeyboardMarkup(resize_keyboard=True)))
    bot.register_next_step_handler(message, lambda message: questionnaire_request(message, user_data, db, bot))


def questionnaire_request(message, user_data, db, bot):
    # Начинаем заполнять анкету
    if message.text == "Да":
        logger.info(f"User {message.chat.id} has started to fill questionnaire")
        edit_profile_questionnaire(message, user_data, db, bot)

    # Отправляем клавиатуру с главным меню без допуска к разделу "Обучение"
    elif message.text == "Нет":
        logger.info(f"User {message.chat.id} has refused to fill questionnaire")
        bot.send_message(message.chat.id, messages.about_questionaire,
                         reply_markup=main_menu_kb(message, types.ReplyKeyboardMarkup(resize_keyboard=True), db))
    else:
        bot.register_next_step_handler(message, lambda message: questionnaire_request(message, user_data, db, bot))
