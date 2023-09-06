import telebot
import config

bot = telebot.TeleBot(config.token, threaded=False)

import handlers

bot.polling(none_stop=True, interval=0)
