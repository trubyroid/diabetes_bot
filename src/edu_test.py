from src.users import Database, connect_db
# from src.keyboards import finish_edu_test_kb
from telebot import types

def edu_test(message, bot):
    chat_id = message.chat.id
    answers = {}
    db = connect_db("users.db")

    bot.send_message(chat_id, 'Чтобы начать тестирование введите: "Начать"')
    bot.register_next_step_handler(message, \
            lambda message: test_question_1(message, answers, db, bot))

    # answers[chat_id] = {'': }

def test_question_1(message, answers, db, bot):
    chat_id = message.chat.id
    question_1 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_2(message, answers, db, bot))
        
    answers[chat_id] = {'question_1': question_1}

def test_question_2(message, answers, db, bot):
    chat_id = message.chat.id
    question_2 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_3(message, answers, db, bot))
        
    answers[chat_id] = {'question_2': question_2}

def test_question_3(message, answers, db, bot):
    chat_id = message.chat.id
    question_3 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_4(message, answers, db, bot))
        
    answers[chat_id] = {'question_3': question_3}

def test_question_4(message, answers, db, bot):
    chat_id = message.chat.id
    question_4 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_5(message, answers, db, bot))
        
    answers[chat_id] = {'question_4': question_4}

def test_question_5(message, answers, db, bot):
    chat_id = message.chat.id
    question_5 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_6(message, answers, db, bot))
        
    answers[chat_id] = {'question_5': question_5}

def test_question_6(message, answers, db, bot):
    chat_id = message.chat.id
    question_6 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_7(message, answers, db, bot))
        
    answers[chat_id] = {'question_6': question_6}

def test_question_7(message, answers, db, bot):
    chat_id = message.chat.id
    question_7 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_8(message, answers, db, bot))
        
    answers[chat_id] = {'question_7': question_7}

def test_question_8(message, answers, db, bot):
    chat_id = message.chat.id
    question_8 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_9(message, answers, db, bot))
        
    answers[chat_id] = {'question_8': question_8}

def test_question_9(message, answers, db, bot):
    chat_id = message.chat.id
    question_9 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_10(message, answers, db, bot))
        
    answers[chat_id] = {'question_9': question_9}

def test_question_10(message, answers, db, bot):
    chat_id = message.chat.id
    question_10 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_11(message, answers, db, bot))
        
    answers[chat_id] = {'question_10': question_10}

def test_question_11(message, answers, db, bot):
    chat_id = message.chat.id
    question_11 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_12(message, answers, db, bot))
        
    answers[chat_id] = {'question_11': question_11}

def test_question_12(message, answers, db, bot):
    chat_id = message.chat.id
    question_12 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_13(message, answers, db, bot))
        
    answers[chat_id] = {'question_12': question_12}

def test_question_13(message, answers, db, bot):
    chat_id = message.chat.id
    question_13 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_14(message, answers, db, bot))
        
    answers[chat_id] = {'question_13': question_13}

def test_question_14(message, answers, db, bot):
    chat_id = message.chat.id
    question_14 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_15(message, answers, db, bot))
        
    answers[chat_id] = {'question_14': question_14}

def test_question_15(message, answers, db, bot):
    chat_id = message.chat.id
    question_15 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_16(message, answers, db, bot))
        
    answers[chat_id] = {'question_15': question_15}

def test_question_16(message, answers, db, bot):
    chat_id = message.chat.id
    question_16 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_17(message, answers, db, bot))
        
    answers[chat_id] = {'question_16': question_16}

def test_question_17(message, answers, db, bot):
    chat_id = message.chat.id
    question_17 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_18(message, answers, db, bot))
        
    answers[chat_id] = {'question_17': question_17}

def test_question_18(message, answers, db, bot):
    chat_id = message.chat.id
    question_18 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_19(message, answers, db, bot))
        
    answers[chat_id] = {'question_18': question_18}

def test_question_19(message, answers, db, bot):
    chat_id = message.chat.id
    question_19 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_20(message, answers, db, bot))
        
    answers[chat_id] = {'question_19': question_19}

def test_question_20(message, answers, db, bot):
    chat_id = message.chat.id
    question_20 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_21(message, answers, db, bot))
        
    answers[chat_id] = {'question_20': question_20}

def test_question_21(message, answers, db, bot):
    chat_id = message.chat.id
    question_21 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_22(message, answers, db, bot))
        
    answers[chat_id] = {'question_21': question_21}

def test_question_22(message, answers, db, bot):
    chat_id = message.chat.id
    question_22 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_23(message, answers, db, bot))
        
    answers[chat_id] = {'question_22': question_22}

def test_question_23(message, answers, db, bot):
    chat_id = message.chat.id
    question_23 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_24(message, answers, db, bot))
        
    answers[chat_id] = {'question_23': question_23}

def test_question_24(message, answers, db, bot):
    chat_id = message.chat.id
    question_24 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_25(message, answers, db, bot))
        
    answers[chat_id] = {'question_24': question_24}

def test_question_25(message, answers, db, bot):
    chat_id = message.chat.id
    question_25 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_26(message, answers, db, bot))
        
    answers[chat_id] = {'question_25': question_25}

def test_question_26(message, answers, db, bot):
    chat_id = message.chat.id
    question_26 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_27(message, answers, db, bot))
        
    answers[chat_id] = {'question_26': question_26}

def test_question_27(message, answers, db, bot):
    chat_id = message.chat.id
    question_27 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_question_28(message, answers, db, bot))
        
    answers[chat_id] = {'question_27': question_27}

def test_question_28(message, answers, db, bot):
    chat_id = message.chat.id
    question_28 = message.text

    bot.send_message(chat_id, 'Введите вашу фамилию:')
    bot.register_next_step_handler(message, lambda message: test_finish(message, answers, db, bot))
        
    answers[chat_id] = {'question_28': question_28}

def test_finish(message, answers, db, bot):
    bot.send_message(message.from_user.id, 'Тестироване окончено.')

