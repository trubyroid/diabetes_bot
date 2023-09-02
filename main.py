import telebot
import config
import requests
from telebot import types
from registerPageUtils import connect_db, process_name_step

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)

@bot.message_handler(commands=['clear_db'])
def clear_db(messege):
    db = connect_db("users.db")
    db.clear_database()

@bot.message_handler(commands=['delete_user'])
def delete_user(messege):
    db = connect_db("users.db")
    bot.send_message(messege.chat.id, 'Введите id пользователя, которого нужно удалить:')
    db.clear_database()

@bot.message_handler(commands=['all'])
def view_all(messege):
    db = connect_db("users.db")
    all_records = db.get_all_records()
    bot.send_message(messege.chat.id, "id | name | surname | email")
    for record in all_records:
        bot.send_message(messege.chat.id, f"{record[0]} | {record[1]} | {record[2]} | {record[3]}")

@bot.message_handler(commands=['register'])
def handle_register(message):
    chat_id = message.chat.id
    users = {}
    db = connect_db("users.db")
    # Запрашиваем имя
    bot.send_message(chat_id, 'Введите ваше имя:')
    bot.register_next_step_handler(message, lambda messege: process_name_step(messege, users, db, bot))

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
    # done
    if message.text == 'Главное меню':
        btn_education = types.KeyboardButton("Обучение")
        btn_profile = types.KeyboardButton("Профиль")
        btn_social_media = types.KeyboardButton('Об онлайн-школе')
        markup.add(btn_education, btn_profile, btn_social_media)
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

    # Обучение
    # done
    elif message.text == 'Обучение':
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

    # Выбрать платформу
    # in progress
    elif message.text == 'Выбрать платформу':
        # keyboard
        markup = types.InlineKeyboardMarkup()
        btn_vk_edu = types.InlineKeyboardButton("Школа диабета VK", url='https://vk.com/video/@shkola.diabeta?section=playlists')
        btn_youtube_edu = types.InlineKeyboardButton("Школа диабета Youtube", url='https://www.youtube.com/playlist?list=PL_dK9vVNI4Vj10OHq4e9pDTqHxpijcTi-')
        btn_dzen_edu = types.InlineKeyboardButton("Школа диабета Dzen", url='https://dzen.ru/dibet')
        markup.add(btn_vk_edu)
        markup.add(btn_youtube_edu)
        markup.add(btn_dzen_edu)
        bot.send_message(message.chat.id, "Программа обучения: https://vk.com/@shkola.diabeta-programma\nНажми на кнопку и перейди на сайт".format(message.from_user), reply_markup=markup)
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_main_menu)
        # messege 
        bot.send_message(message.from_user.id, 'Чтобы вернуться назад нажмите - /back', reply_markup=markup)

    # Об онлайн-школе
    # in progress
    elif message.text == 'Об онлайн-школе':
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_main_menu)
        # markup = markup
        # messege
        bot.send_message(message.from_user.id, config.online_school_description, reply_markup=markup)

    elif message.text == 'Профиль':
        btn_show_profile = types.KeyboardButton('Посмотреть профиль')
        btn_edit_profile = types.KeyboardButton('Редактировать профиль')
        markup.add(btn_show_profile, btn_edit_profile)

        bot.send_message(message.from_user.id, config.profile_section, reply_markup=markup)
    # Некорректный ввод
    # done
    else:
        bot.send_message(message.from_user.id, "Такой команды нет. Введите корректную команду.")


bot.polling(none_stop=True, interval=0)
