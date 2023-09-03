from telebot import types
import config


def main_menu_kb(message, markup, bot):
    btn_education = types.KeyboardButton("Обучение")
    btn_profile = types.KeyboardButton("Профиль")
    btn_social_media = types.KeyboardButton('Об онлайн-школе')
    markup.add(btn_education, btn_profile, btn_social_media)

    bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)


def education_kb(message, markup, bot):
    btn_choose = types.KeyboardButton('Выбрать платформу')
    btn_get_homework = types.KeyboardButton('Получить домашнее задание')
    btn_pass_homework = types.KeyboardButton('Пройти тестирование')
    btn_progress = types.KeyboardButton('Прогресс')  # in future
    btn_need_help = types.KeyboardButton('Нужна помощь')
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_choose, btn_get_homework, btn_pass_homework, btn_progress, btn_need_help, btn_main_menu)

    bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)


def choose_platform_kb(message, markup, bot):
    markup = types.InlineKeyboardMarkup()
    btn_vk_edu = types.InlineKeyboardButton("VK",
                                            url='https://vk.com/video/@shkola.diabeta?section=playlists')
    btn_youtube_edu = types.InlineKeyboardButton("Youtube",
                                                 url='https://www.youtube.com/playlist?list=PL_dK9vVNI4Vj10OHq4e9pDTqHxpijcTi-')
    btn_dzen_edu = types.InlineKeyboardButton("Dzen", url='https://dzen.ru/dibet')
    markup.add(btn_vk_edu)
    markup.add(btn_youtube_edu)
    markup.add(btn_dzen_edu)
    bot.send_message(message.chat.id,
                     "Программа обучения: https://vk.com/@shkola.diabeta-programma\nНажми на кнопку и перейди на сайт".format(
                         message.from_user), reply_markup=markup)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_main_menu)

    bot.send_message(message.from_user.id, 'Чтобы вернуться назад нажмите - /back', reply_markup=markup)


def about_school_kb(message, markup, bot):
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_main_menu)
    bot.send_message(message.from_user.id, config.online_school_description, reply_markup=markup)


def profile_kb(message, markup, bot):
    btn_show_profile = types.KeyboardButton('Посмотреть профиль')
    btn_edit_profile = types.KeyboardButton('Редактировать профиль')
    btn_get_back = types.KeyboardButton('Главное меню')
    markup.add(btn_show_profile, btn_edit_profile, btn_get_back)

    bot.send_message(message.from_user.id, config.profile_section, reply_markup=markup)

# def finish_edu_test_kb(message, markup, bot):
#     btn_education = types.KeyboardButton("Обучение")
#     btn_main_menu = types.KeyboardButton('Главное меню')
#     markup.add(btn_education, btn_main_menu)

#     bot.send_message(message.from_user.id, '👀 Выберите вариант из списка.', reply_markup=markup)