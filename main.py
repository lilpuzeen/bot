import telebot
import time
from telebot import types
from selenium import webdriver

bot = telebot.TeleBot("1936862836:AAEkdp3-01lk0WQOoRILooZUAA1SVy3XLoE")

problem_number = 0
PROBLEMS = {1: 'Простейшие текстовые задачи',
            2: 'Чтение графиков и диаграмм',
            3: 'Квадратная решётка, координатная плоскость',
            4: 'Начала теории вероятностей',
            5: 'Простейшие уравнения',
            6: 'Планиметрия',
            7: 'Производная и первообразная',
            8: 'Стереометрия',
            9: 'Вычисления и преобразования',
            10: 'Задачи с прикладным содержанием',
            11: 'Текстовые задачи',
            12: 'Наибольшее и наименьшее значение функций',
            13: 'Уравнения',
            14: 'Стереометрическая задача',
            15: 'Неравенства',
            16: 'Планиметрическая задача',
            17: 'Финансовая математика',
            18: 'Задача с параметром',
            19: 'Числа и их свойства'}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(key_no)
    bot.send_message(message.from_user.id, "Дарова заебал! Хочешь матеши?", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    while True:
        if call.data == "yes":
            bot.send_message(call.message.chat.id, "Напиши номер задания!")
            bot.register_next_step_handler(call.message, choose_number_problem)
            break
        elif call.data == "no":
            bot.send_message(call.message.chat.id, "Ну и пошел нахуй!")
            bot.register_next_step_handler(call.message, send_welcome)
            break


def choose_number_problem(message):
    global problem_number
    problem_number = message.text
    bot.send_message(message.from_user.id, f"Окей долбаеб, ты выбрал тему {PROBLEMS[int(problem_number)]}! Подожди немного!")
    time.sleep(2)
    bot.register_next_step_handler(message, show_problem)


def show_problem(message):  # TODO подключить класс из parser.py. Подумать над подключением сервака
    # TODO Посмотреть почему даблит некоторые сообщения!
    # TODO провести анализ на наличие фотографий в задании.
    # TODO в классе GetProblem есть метод getimage. Поработать над его подключением и отправкой фото заданий через screenshot_as_png
    bot.send_message(message.from_user.id, "Done!")

bot.polling()
