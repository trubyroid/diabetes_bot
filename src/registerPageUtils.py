from telebot import types
from src.keyboards import main_menu_kb
from src.profile import edit_profile_questionnaire
from src.database import Database
import config
from main import logger as logger


def questionnaire_request(message, db, bot):
    if message.text == "Да":
        logger.info(f"User {message.from_user.id} has started to fill questionnaire")
        edit_profile_questionnaire(message, db, bot)
    elif message.text == "Нет":
        logger.info(f"User {message.from_user.id} has refused to fill questionnaire")
        bot.send_message(message.chat.id, config.about_questionaire, reply_markup=types.ReplyKeyboardRemove())
        main_menu_kb(message, types.ReplyKeyboardMarkup(resize_keyboard=True), bot)
    else:
        bot.register_next_step_handler(message, lambda message: questionnaire_request(message, db, bot))


def process_name_step(message, users, db, bot):
    chat_id = message.chat.id
    name = message.text

    # Запрашиваем фамилию
    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: process_surname_step(message, users, db, bot))

    # Сохраняем имя
    users[chat_id]['name'] = name

def process_surname_step(message, users, db, bot):
    chat_id = message.chat.id
    surname = message.text

    # Добавляем фамилию
    users[chat_id]['surname'] = surname

    # Запрашиваем почту
    bot.send_message(chat_id, 'Введите вашу почту:')
    bot.register_next_step_handler(message, lambda message: process_email_step(message, users, db, bot))


def process_email_step(message, users, db, bot):
    chat_id = message.chat.id
    email = message.text

    # Сохраняем почту
    users[chat_id]['email'] = email

    # Выводим информацию о пользователе
    user_info = users[chat_id]

    # Сохраняем информацию в базу данных
    db.insert_partial_user(chat_id, user_info['name'], user_info['surname'], user_info['email'])

    logger.info(f"User {message.from_user.id} has finished registration")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_no = types.KeyboardButton('Нет')
    btn_yes = types.KeyboardButton('Да')
    markup.add(btn_yes, btn_no)
    bot.send_message(chat_id, config.questionnaire_request, reply_markup=markup)
    bot.register_next_step_handler(message, lambda message: questionnaire_request(message, db, bot))
