"""
В этом модуле реализован процесс тестирования пользователя.
Результаты записываются в отдельную таблицу в базе данных.
Подразумевается, что в дальнейшем они будут использованы для формирования рекомендаций.
"""

from main import logger as logger
from src.keyboards import go_back_kb, test_answers_kb


def start_testing(message, markup, db, bot):

    logger.info(f"User {message.from_user.id} has started to go through the test")

    chat_id = message.chat.id
    answers = [chat_id]

    bot.send_message(chat_id, 'Что происходит с сахаром крови при недостатке инсулина\n\n'
                              '1) Cахар крови повышается\n'
                              '2) Cахар крови понижается\n'
                              '3) Сахар крови остаётся без изменений', reply_markup=test_answers_kb())
    bot.register_next_step_handler(message, lambda message: test_question_2(message, answers, markup, db, bot))


def test_question_2(message, answers, markup, db, bot):
    if message.text not in ("1", "2", "3"):
        start_testing(message, markup, db, bot)
    else:
        chat_id = message.chat.id
        answers.append(message.text)

        bot.send_message(chat_id, 'Что будет с больным СД молодого возраста, '
                                  'если в течение недели он не будет вводить инсулин?\n\n'
                                  '1) Диабетический кетоацидоз/кома\n'
                                  '2) Гипогликемия\n'
                                  '3) Ничего не произойдёт', reply_markup=test_answers_kb())
        bot.register_next_step_handler(message, lambda message: test_question_3(message, answers, markup, db, bot))


def test_question_3(message, answers, markup, db, bot):
    if message.text not in ("1", "2", "3"):
        test_question_2(message, answers, markup, db, bot)
    else:
        chat_id = message.chat.id
        answers.append(message.text)

        bot.send_message(chat_id, ' Укажите признак гипогликемии, который'
                                  ' могут заметить у вас со стороны (другие люди)?\n\n'
                                  '1) Отдышка\n'
                                  '2) Отёк кожи\n'
                                  '3) Дрожание рук', reply_markup=test_answers_kb())
        bot.register_next_step_handler(message, lambda message: test_finish(message, answers, markup, db, bot))


def test_finish(message, answers, markup, db, bot):
    if message.text not in ("1", "2", "3"):
        test_question_3(message, answers, markup, db, bot)
    else:
        answers.append(message.text)
        logger.info(f"User {message.from_user.id} has finished the test")
        bot.send_message(message.from_user.id, 'Тестирование окончено.', reply_markup=go_back_kb(markup))

        db.insert_user_answers(answers)

