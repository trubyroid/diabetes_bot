from telebot import types
import config
from main import bot as bot
from main import logger as logger

from src.profile import edit_profile, show_profile
from src.registerPageUtils import process_name_step
from src.keyboards import main_menu_kb, education_kb, choose_platform_kb, about_school_kb, profile_kb, go_back_kb
from src.edu_test import start_testing
from src.database import connect_db


# Начало работы с ботом
@bot.message_handler(commands=['start'])
def start_user_flow(message):
    logger.info(f"User {message.from_user.id} has started work with bot")
    connect_db()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_reg = types.KeyboardButton("Зарегистрироваться")
    markup.add(btn_reg)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)
    bot.register_next_step_handler(message, register)


# Остановка работы бота
@bot.message_handler(commands=['stop'])
def stop_user_flow(message):
    logger.info(f"User {message.from_user.id} has finished work with bot")

# Запуск регистрации
@bot.message_handler(commands=['register'])
def register(message):
    if message.text == "Зарегистрироваться":
        chat_id = message.chat.id
        users = {chat_id: {}}
        db = connect_db()
        logger.info(f"User {chat_id} has started registration")
        bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda message: process_name_step(message, users, db, bot))
    else:
        bot.register_next_step_handler(message, register)


# Обработчик основных текстовых запросов пользователя
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    db = connect_db()
    chat_id = message.chat.id

    if message.text == 'Главное меню':
        bot.send_message(chat_id, config.main_section, reply_markup=main_menu_kb(message, markup, db))

    elif message.text == 'Обучение':
        bot.send_message(chat_id, config.edu_section, reply_markup=education_kb(markup))

    elif message.text == 'Об онлайн-школе':
        bot.send_message(chat_id, config.online_school_description, reply_markup=about_school_kb(markup))

    elif message.text == 'Выбрать платформу':
        bot.send_message(chat_id, config.edu_programm.format(message.from_user), reply_markup=choose_platform_kb())
        bot.send_message(chat_id, config.go_back_message, reply_markup=go_back_kb(markup))

    elif message.text == 'Профиль':
        bot.send_message(chat_id, config.profile_section, reply_markup=profile_kb(markup))

    elif message.text == 'Пройти тестирование':
        start_testing(message, markup, db, bot)

    elif message.text == "Посмотреть профиль":
        show_profile(message, db, bot)

    elif message.text == 'Редактировать профиль':
        edit_profile(message, db, bot)

    # Заглушка
    elif message.text == 'Прогресс':
        bot.send_message(chat_id, config.progress_stub)

    # Некорректный ввод
    else:
        bot.send_message(chat_id, config.incorrect_input)



# @bot.message_handler(commands=['clear_db'])
# def clear_db(message):
#     db = connect_db("users.db")
#     db.clear_database()
#
# @bot.message_handler(commands=['delete_user'])
# def delete_user(message):
#     db = connect_db("users.db")
#     bot.send_message(message.chat.id, 'Введите id пользователя, которого нужно удалить:')
#     bot.register_next_step_handler(message, lambda message: db.delete_user(message.text) )
#
# @bot.message_handler(commands=['all'])
# def view_all(messege):
#     db = connect_db("users.db")
#     all_records = db.get_all_records()
#     bot.send_message(messege.chat.id, "id | name | surname | email")
#     for record in all_records:
#         bot.send_message(messege.chat.id, f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")
