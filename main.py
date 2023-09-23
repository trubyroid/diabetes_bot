import logging
import telebot

import os
from dotenv import load_dotenv

# Загружаем токен из файла с переменными среды
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
token = os.environ['TOKEN']

# Создание и настройка логгера
telebot.logging.basicConfig(filename="users_history.log",
               format='%(asctime)s %(levelname)s %(message)s',
               datefmt='%d-%b-%y %H:%M:%S',
               filemode='w')
logger = telebot.logger
logger.setLevel(logging.INFO)

# Создание и запуск бота
bot = telebot.TeleBot(token, threaded=False)

import handlers

bot.polling(non_stop=True, interval=0)
