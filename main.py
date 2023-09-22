import telebot
import config
import logging

logging.basicConfig(filename="users_history.log",
               format='%(asctime)s %(levelname)s %(message)s',
               datefmt='%d-%b-%y %H:%M:%S',
               filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


bot = telebot.TeleBot(config.token, threaded=False)
logger.info("The bot has started")

import handlers

bot.polling(none_stop=True, interval=0)
#user_logger.info("The bot has finished.")
