"""
В этом модуле представлены все используемые клавиатуры.
"""

from telebot import types
import config
from src.database import find_user_by_chat_id


def main_menu_kb(message, markup, db):
    btns = []

    if find_user_by_chat_id(message.chat.id, db)["access"]:
        btns.append(types.KeyboardButton("Обучение"))
    btns.append(types.KeyboardButton("Профиль"))
    btns.append(types.KeyboardButton('Об онлайн-школе'))

    for btn in btns:
        markup.add(btn)
    return markup


def education_kb(markup):
    btn_choose = types.KeyboardButton('Выбрать платформу')
    btn_testing = types.KeyboardButton('Пройти тестирование')
    btn_main_menu = types.KeyboardButton('Главное меню')
    btn_progress = types.KeyboardButton('Прогресс')
    markup.add(btn_choose, btn_testing, btn_main_menu, btn_progress)
    return markup


def choose_platform_kb():
    markup = types.InlineKeyboardMarkup()
    btn_vk_edu = types.InlineKeyboardButton("VK",
                                            url='https://vk.com/video/@shkola.diabeta?section=playlists')
    btn_youtube_edu = types.InlineKeyboardButton("Youtube",
                                                 url='https://www.youtube.com/playlist?list=PL_dK9vVNI4Vj10OHq4e9pDTqHxpijcTi-')
    btn_dzen_edu = types.InlineKeyboardButton("Dzen", url='https://dzen.ru/dibet')
    markup.add(btn_vk_edu)
    markup.add(btn_youtube_edu)
    markup.add(btn_dzen_edu)
    return markup

def go_back_kb(markup):
    btn_main_menu = types.KeyboardButton('Главное меню')
    btn_education = types.KeyboardButton('Обучение')
    markup.add(btn_main_menu, btn_education)
    return markup



def about_school_kb(markup):
    btn_main_menu = types.KeyboardButton('Главное меню')
    markup.add(btn_main_menu)
    return markup


def profile_kb(markup):
    btn_show_profile = types.KeyboardButton('Посмотреть профиль')
    btn_edit_profile = types.KeyboardButton('Редактировать профиль')
    btn_get_back = types.KeyboardButton('Главное меню')
    markup.add(btn_show_profile, btn_edit_profile, btn_get_back)
    return markup


def test_answers_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_one = types.KeyboardButton('1')
    btn_two = types.KeyboardButton('2')
    btn_three = types.KeyboardButton('3')
    markup.add(btn_one, btn_two, btn_three)
    return markup
