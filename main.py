import telebot
import config
from telebot import types
from src.registerPageUtils import connect_db, process_name_step, handler_questionnaire
from src.keyboards import main_menu_kb, education_kb, choose_platform_kb, about_school_kb, profile_kb

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_reg = types.KeyboardButton("Зарегистрироваться")
    markup.add(btn_reg)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)
    bot.register_next_step_handler(message, handle_register)


@bot.message_handler(commands=['clear_db'])
def clear_db(message):
    db = connect_db("users.db")
    db.clear_database()

@bot.message_handler(commands=['delete_user'])
def delete_user(message):
    db = connect_db("users.db")
    bot.send_message(message.chat.id, 'Введите id пользователя, которого нужно удалить:')
    bot.register_next_step_handler(message, lambda message: db.delete_user(message.text) )

@bot.message_handler(commands=['all'])
def view_all(messege):
    db = connect_db("users.db")
    all_records = db.get_all_records()
    bot.send_message(messege.chat.id, "id | name | surname | email")
    for record in all_records:
        bot.send_message(messege.chat.id, f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")

@bot.message_handler(commands=['register'])
def handle_register(message):
    if message.text == "Зарегистрироваться":
        chat_id = message.chat.id
        users = {message.chat.id: {}}
        db = connect_db("users.db")
        # Запрашиваем имя
        bot.send_message(chat_id, 'Введите ваше имя:', reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, lambda messege: process_name_step(messege, users, db, bot))
    else:
        bot.register_next_step_handler(message, handle_register)

@bot.message_handler(commands=['back'])
def back(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_choose = types.KeyboardButton('Выбрать платформу')
    btn_get_homework = types.KeyboardButton('Получить домашнее задание')
    btn_pass_homework = types.KeyboardButton('Сдать домашнее задание')
    btn_progress = types.KeyboardButton('Прогресс')               # in future
    btn_need_help = types.KeyboardButton('Нужна помощь')
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_choose, btn_get_homework, btn_pass_homework, btn_progress, btn_need_help, btn_main_menu)
    # messege
    bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

# Handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Главное меню
    if message.text == 'Главное меню':
        main_menu_kb(message, markup, bot)

    # Обучение
    elif message.text == 'Обучение':
        education_kb(message, markup, bot)

    # Выбрать платформу
    # in progress
    elif message.text == 'Выбрать платформу':
        choose_platform_kb(message, markup, bot)

    # Об онлайн-школе
    # in progress
    elif message.text == 'Об онлайн-школе':
        about_school_kb(message, markup, bot)

    elif message.text == 'Профиль':
        profile_kb(message, markup, bot)
    elif message.text == 'Редактировать профиль':
        bot.register_next_step_handler(message, lambda message: handler_questionnaire(message, bot))

    # Некорректный ввод
    # done
    else:
        bot.send_message(message.from_user.id, "Такой команды нет. Введите корректную команду.")


bot.polling(none_stop=True, interval=0)
