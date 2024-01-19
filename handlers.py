from telebot import types
import messages
from main import bot as bot
from main import logger as logger

from src.profile import edit_profile, show_profile
from src.registerPageUtils import process_name_step

from src.keyboards import main_menu_kb, education_kb, choose_platform_kb,\
    about_school_kb, profile_kb, go_back_kb, start_kb

from src.edu_test import start_testing
from src.database import connect_db


# Начало работы с ботом
@bot.message_handler(commands=['start'])
def start_user_flow(message):
    logger.info(f"User {message.chat.id} has started working with bot")

    bot.send_message(message.chat.id, messages.greetings, reply_markup=start_kb())
    bot.register_next_step_handler(message, register)


# Остановка и рестарт бота
@bot.message_handler(commands=['stop'])
def stop_user_flow(message):
    logger.info(f"User {message.chat.id} has finished working with bot")

    db = connect_db()
    db.delete_user(message.chat.id)

    bot.send_message(message.chat.id, messages.restart)


# Запуск регистрации
@bot.message_handler(commands=['register'])
def register(message):
    if message.text == "Зарегистрироваться":
        chat_id = message.chat.id
        user_data = {}
        db = connect_db()

        logger.info(f"User {chat_id} has started registration")

        bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda message: process_name_step(message, user_data, db, bot))
    else:
        bot.register_next_step_handler(message, register)


# Обработчик основных текстовых запросов. Навигация по разделам.
@bot.message_handler(content_types=['text'])
def handle_text_messages(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    db = connect_db()
    chat_id = message.chat.id

    if message.text == 'Главное меню':
        bot.send_message(chat_id, messages.main_section, reply_markup=main_menu_kb(message, markup, db))

    elif message.text == 'Обучение':
        bot.send_message(chat_id, messages.edu_section, reply_markup=education_kb(markup))

    elif message.text == 'Об онлайн-школе':
        bot.send_message(chat_id, messages.online_school_description, reply_markup=about_school_kb(markup))

    elif message.text == 'Выбрать платформу':
        # Инлайн клавиатура с платформами
        bot.send_message(chat_id, messages.edu_programm.format(message.from_user), reply_markup=choose_platform_kb())
        # Клавиатура с возможностью вернуться в один из предыдущих разделов
        bot.send_message(chat_id, messages.go_back_message, reply_markup=go_back_kb(markup))

    elif message.text == 'Профиль':
        bot.send_message(chat_id, messages.profile_section, reply_markup=profile_kb(markup))

    elif message.text == 'Пройти тестирование':
        start_testing(message, markup, db, bot)

    elif message.text == "Посмотреть профиль":
        show_profile(message, db, bot)

    elif message.text == 'Редактировать профиль':
        edit_profile(message, db, bot)

    # Заглушка
    elif message.text == 'Рекомендации':
        bot.send_message(chat_id, messages.progress_stub)

    # Некорректный ввод
    else:
        bot.send_message(chat_id, messages.incorrect_input)
