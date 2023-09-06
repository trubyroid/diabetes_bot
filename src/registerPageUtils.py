from src.users import Database, connect_db
from telebot import types
from src.keyboards import main_menu_kb
from src.profile import edit_profile_questionnaire
from src.users import Database
import config


def questionnaire(message, bot):
    if message.text == "Да":
        edit_profile_questionnaire(message, bot)
    elif message.text == "Нет":
        bot.send_message(message.chat.id, config.about_questionaire, reply_markup=types.ReplyKeyboardRemove())
        main_menu_kb(message, types.ReplyKeyboardMarkup(resize_keyboard=True), bot)
    else:
        bot.register_next_step_handler(message, lambda message: questionnaire(message, bot))


def process_name_step(message, users, db, bot):
    chat_id = message.chat.id
    name = message.text

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: process_surname_step(message, users, bot))

    # Сохраняем имя
    users[chat_id] = {'name': name}

def process_surname_step(message, users, bot):
    chat_id = message.chat.id
    surname = message.text

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda message: process_email_step(message, users, bot))

    # Добавляем фамилию
    users[chat_id]['surname'] = surname

def process_email_step(message, users, bot):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    users[chat_id]['email'] = email

    # Выводим информацию о пользователе
    user_info = users[chat_id]

    # Сохраняем информацию в базу данных
    db = Database("users.db")
    db.insert_partial_user(chat_id, user_info['name'], user_info['surname'], user_info['email'])

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_no = types.KeyboardButton('Нет')
    btn_yes = types.KeyboardButton('Да')
    markup.add(btn_yes, btn_no)
    bot.send_message(chat_id, config.questionnaire_request, reply_markup=markup)
    bot.register_next_step_handler(message, lambda message: questionnaire(message, bot))
