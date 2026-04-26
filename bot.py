
import sqlite3

from data1 import get_all_data
import telebot
import config
import data1
data1.create_table()
data1.create_log
bot = telebot.TeleBot(config.API_TOKEN)
#кнопочки :)#
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item0 = telebot.types.KeyboardButton("I am a teacher")
    item1 = telebot.types.KeyboardButton("when is the next lesson?")
    item2 = telebot.types.KeyboardButton("what group am i in?")
    item5 = telebot.types.KeyboardButton("What day is the lesson?")
    item3 = telebot.types.KeyboardButton("what class do i have?")
    item4 = telebot.types.KeyboardButton("show all data")
    markup.add(item0, item1, item2, item5, item3, item4)
    bot.send_message(message.chat.id, "choose an option", reply_markup=markup)
#Вопросики#
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "I am a teacher":
        send_password(message)
    elif message.text == "when is the next lesson?":
        check_timetable(message)
    elif message.text == "what group am i in?":
        check_group(message)
    elif message.text == "What day is the lesson?":
        check_day(message)
    elif message.text == "what class do i have?":
        check_class(message)
    elif message.text == "show all data":
        show_all_data(message)
    else:
        bot.send_message(message.chat.id, "Please use the buttons below:")
#Ответы :o#
def send_password(message):
    bot.send_message(message.chat.id, "Please enter the password:")
    bot.register_next_step_handler(message, check_password)

def check_password(message):
    password = message.text.strip()
    if password == "12345":
        bot.send_message(message.chat.id, "Access granted! You can now add data.")
        bot.send_message(message.chat.id, "Please enter the lesson name:")
        bot.register_next_step_handler(message, get_lesson_name_step)
    else:
        bot.send_message(message.chat.id, "Access denied! Incorrect password.")

def get_lesson_name_step(message):
    lesson = message.text.strip()
    bot.send_message(message.chat.id, "Please enter the group:")
    bot.register_next_step_handler(message, get_group_step, lesson)

def get_group_step(message, lesson):
    group = message.text.strip()
    bot.send_message(message.chat.id, "Please enter the day:")   
    bot.register_next_step_handler(message, get_day_step, lesson, group)

def get_day_step(message, lesson, group):
    day = message.text.strip()
    bot.send_message(message.chat.id, "Please enter the timetable:")
    bot.register_next_step_handler(message, get_timetable_step, lesson, group, day)

def get_timetable_step(message, lesson, group, day):
    timetable = message.text.strip()
    bot.send_message(message.chat.id, "Please enter the name:")
    bot.register_next_step_handler(message, get_name_step, lesson, group, day, timetable)

def get_name_step(message, lesson, group, day, timetable):
    student = message.text.strip()
    data1.create_log(lesson, group, day, timetable, student)
    bot.send_message(message.chat.id, "Data added successfully!")

def check_timetable(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer1)

def answer1(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[4]
        timetable = row[3]
        if student == name:
            bot.send_message(message.chat.id, f"Your next lesson is at: {timetable} good luck!")
            found = True
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")

def check_group(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer2)

def answer2(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[4]
        group = row[1]
        if student == name:
            bot.send_message(message.chat.id, f"You're in group: {group} intresting<:0")
            found = True
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")

def check_day(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer5)

def answer5(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[4]
        day = row[2]
        if student == name:
            bot.send_message(message.chat.id, f"Your lesson is on: {day} have a nice day!")
            found = True
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")

def check_class(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer3)



def answer3(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[4]
        lesson = row[0]
        if student == name:
            bot.send_message(message.chat.id, f"You're in class: {lesson} great choice!")
            found = True
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")

def show_all_data(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer4)

def answer4(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[4]
        lesson = row[0]
        timetable = row[3]
        group = row[1]
        day = row[2]
        if student == name:
            bot.send_message(message.chat.id, f"All info: {student}, {lesson}, {timetable}, {group}, {day} wow thats a lot!")
            found = True
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")
bot.infinity_polling()