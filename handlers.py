from telebot import types
import threading
import config
from main import bot as bot

from src.profile import edit_profile, show_profile
from src.registerPageUtils import process_name_step
from src.keyboards import main_menu_kb, education_kb, choose_platform_kb, about_school_kb, profile_kb
from src.edu_test import edu_test
from src.users import connect_db


@bot.message_handler(commands=['start'])
def start_user_flow(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_reg = types.KeyboardButton("Зарегистрироваться")
    markup.add(btn_reg)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)
    bot.register_next_step_handler(message, register)


@bot.message_handler(commands=['register'])
def register(message):
    if message.text == "Зарегистрироваться":
        chat_id = message.chat.id
        users = {message.chat.id: {}}
        db = connect_db("users.db")
        bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda messege: process_name_step(messege, users, db, bot))
    else:
        bot.register_next_step_handler(message, register)


# Text message handler
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Главное меню
    # done
    if message.text == 'Главное меню':
        main_menu_kb(message, markup, bot)

    # Обучение
    # in progress
    elif message.text == 'Обучение':
        education_kb(message, markup, bot)

    # Выбрать платформу
    elif message.text == 'Выбрать платформу':
        choose_platform_kb(message, markup, bot)

    # Пройти тестирование
    elif message.text == 'Пройти тестирование':
        edu_test(message, bot)

    # Об онлайн-школе
    # done
    elif message.text == 'Об онлайн-школе':
        about_school_kb(message, markup, bot)

    elif message.text == 'Профиль':
        profile_kb(message, markup, bot)
    elif message.text == "Посмотреть профиль":
        show_profile(message, bot)
    elif message.text == 'Редактировать профиль':
        edit_profile(message, bot)
    # Некорректный ввод
    # done
    else:
        bot.send_message(message.from_user.id, "Такой команды нет. Введите корректную команду.")


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
