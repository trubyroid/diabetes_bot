import telebot
from telebot import types

token = '6485464249:AAFogogiykRxigsXkx-l6uaFi9xQ5Ui7YwM'  # Personal token
bot = telebot.TeleBot(token)


# /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Главное меню")
    markup.add(btn)
    bot.send_message(message.from_user.id, "👋 Вас приветствует бот для того, чтобы стать добрее =)",
                     reply_markup=markup)


# /help
@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/start')
    markup.add(btn1)
    bot.reply_to(message, "Бот поможет Вам стать добрее.\nВведите /start чтобы стать добрее.", reply_markup=markup)


# Handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # #Список запросов
    if message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Пройти обучение")
        btn2 = types.KeyboardButton("Получить домашнее задание")
        btn3 = types.KeyboardButton('Отправить домашнее задание')
        btn4 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

    # Пройти обучение
    elif message.text == 'Пройти обучение':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Главное меню")
        markup.add(btn1)
        markup = markup
        bot.send_message(message.from_user.id, "Здесь будет список платформ для обучения", reply_markup=markup)

    elif message.text == 'Получить домашнее задание':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Главное меню")
        markup.add(btn1)
        markup = markup
        # messege
        bot.send_message(message.from_user.id, "Держи домашку =P", reply_markup=markup)

    elif message.text == 'Отправить домашнее задание':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Главное меню")
        markup.add(btn1)
        markup = markup
        # messege
        bot.send_message(message.from_user.id, "Гони домашку =P", reply_markup=markup)

    # Anyway
    else:
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton("/help")
        markup.add(btn)
        # messege
        bot.send_message(message.from_user.id, "Такой команды нет. Введите команду /help.", reply_markup=markup)


# Non-stop polling
bot.polling(none_stop=True, interval=0)
