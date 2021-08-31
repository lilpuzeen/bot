import telebot
import time
from telebot import types
from selenium import webdriver
from parser import GetProblem

bot = telebot.TeleBot("1936862836:AAEkdp3-01lk0WQOoRILooZUAA1SVy3XLoE")


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

woimage = [1, 2, 4, 7, 8, 11, 12, 13, 14, 15, 16, 17, 18]
withimage = [3, 5, 6, 9, 19]


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
    bot.send_message(message.from_user.id, f"Окей долбаеб, ты выбрал тему {PROBLEMS[int(problem_number)]}! Отправь любое сообщение!")
    time.sleep(2)
    bot.register_next_step_handler(message, show_problem)


def show_problem(message):
    global prob_solution
    PROBLEM = GetProblem()
    if problem_number in withimage:
        prob_contruction = PROBLEM.construct()
        prob_image = PROBLEM.getimage()
        prob_solution = PROBLEM.getsolution()
        bot.send_photo(message.from_user.id, prob_contruction)
        bot.send_photo(message.from_user.id, prob_image)
    else:
        prob_contruction = PROBLEM.construct()
        prob_solution = PROBLEM.getsolution()
        bot.send_photo(message.from_user.id, prob_contruction)
    bot.send_message(message.from_user.id, "Done!")


@bot.message_handler(commands=['solution'])
def show_solution(message):
    bot.send_photo(message.from_user.id, prob_solution)
    bot.stop_polling()


bot.polling()
