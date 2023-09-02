import telebot
import config
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, config.greetings, reply_markup=markup)

@bot.message_handler(commands=['register'])
def register(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = "Здесь нужно будет зарегистрироваться."
    btn = types.KeyboardButton("Главное меню")
    markup.add(btn)
    bot.send_message(message.from_user.id, text, reply_markup=markup)

# Handler
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    # Главное меню
    #
    if message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_education = types.KeyboardButton("Пройти обучение")
        btn_profile = types.KeyboardButton("Профиль")
        btn_social_media = types.KeyboardButton('Об онлайн-школе')
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_education, btn_profile, btn_social_media, btn_main_menu)
        bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)

    # Об онлайн-школе
    # in progress
    elif message.text == 'Об онлайн-школе':
        # keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_main_menu = types.KeyboardButton('Главное меню')
        markup.add(btn_main_menu)
        markup = markup
        # messege
        bot.send_message(message.from_user.id, config.online_school_description, reply_markup=markup)

    # Некорректный ввод
    # done
    else:
        # messege
        bot.send_message(message.from_user.id, "Такой команды нет. Введите корректную команду.")

bot.polling(none_stop=True, interval=0)
