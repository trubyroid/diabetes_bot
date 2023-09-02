import telebot
import config
from telebot import types
from registerPageUtils import connect_db, process_name_step

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_reg = types.KeyboardButton("Зарегистрироваться")
    markup.add(btn_reg)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)
    bot.register_next_step_handler(message, handle_register)


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
    if message.text == "Зарегистрироваться":
        chat_id = message.chat.id
        users = {}
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
    btn_need_help = types.KeyboardButton('Нужна помощь')
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_choose, btn_get_homework, btn_pass_homework, btn_need_help, btn_main_menu)
    # messege
    bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)


# Handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Главное меню
    # done
    if message.text == 'Главное меню':
        btn_education = types.KeyboardButton("Пройти обучение")
        btn_profile = types.KeyboardButton("Профиль")
        btn_social_media = types.KeyboardButton('Об онлайн-школе')
        markup.add(btn_education, btn_profile, btn_social_media)
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

    # Обучение
    # done
    elif message.text == 'Пройти обучение':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_choose = types.KeyboardButton('Выбрать платформу')
        btn_get_homework = types.KeyboardButton('Получить домашнее задание')
        btn_pass_homework = types.KeyboardButton('Сдать домашнее задание')
        btn_need_help = types.KeyboardButton('Нужна помощь')
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_choose, btn_get_homework, btn_pass_homework, btn_need_help, btn_main_menu)
        # messege
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

    # Выбрать платформу
    # in progress
    elif message.text == 'Выбрать платформу':
        # keyboard
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Сайт VK", url='https://vk.com/shkola.diabeta')
        markup.add(button1)
        bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
        # messege
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.\nЧтобы вернуться назад нажмите - /back', reply_markup=markup)

    # Об онлайн-школе
    # in progress
    elif message.text == 'Об онлайн-школе':
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_main_menu)
        bot.send_message(message.from_user.id, config.online_school_description, reply_markup=markup)

    elif message.text == 'Профиль':
        btn_show_profile = types.KeyboardButton('Посмотреть профиль')
        btn_edit_profile = types.KeyboardButton('Редактировать профиль')
        btn_get_back = types.KeyboardButton('Главное меню')
        markup.add(btn_show_profile, btn_edit_profile, btn_get_back)

        bot.send_message(message.from_user.id, config.profile_section, reply_markup=markup)
    # Некорректный ввод
    # done
    else:
        bot.send_message(message.from_user.id, "Такой команды нет. Введите корректную команду.")


bot.polling(none_stop=True, interval=0)
