import telebot
import config
import logging

# Создание и настройка логгера
telebot.logging.basicConfig(filename="users_history.log",
               format='%(asctime)s %(levelname)s %(message)s',
               datefmt='%d-%b-%y %H:%M:%S',
               filemode='w')
logger = telebot.logger
logger.setLevel(logging.INFO)


# Создание и запуск бота
bot = telebot.TeleBot(config.token, threaded=False)

import handlers

bot.polling(non_stop=True, interval=0)
