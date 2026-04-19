from data1 import get_all_data
import telebot
import config


bot = telebot.TeleBot(config.API_TOKEN)
#кнопочки :)#
@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("when is the next lesson?")
    item2 = telebot.types.KeyboardButton("what group am i in?")
    item3 = telebot.types.KeyboardButton("what class do i have?")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "choose an option", reply_markup=markup)
#Вопросики#
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    if message.text == "when is the next lesson?":
        check_timetable(message)
    elif message.text == "what group am i in?":
        check_group(message)
    elif message.text == "what class do i have?":
        check_class(message)
    elif message.text == "show all data":
        show_all_data(message)
    else:
        bot.send_message(message.chat.id, "Please use the buttons below:")
#Ответы :o#
def check_timetable(message):
    bot.send_message(message.chat.id, "Please enter your name:")
    bot.register_next_step_handler(message, answer1)

def answer1(message):
    name = message.text.strip()
    data = get_all_data()
    found = False
    for row in data:
        student = row[3]
        timetable = row[2]
        if student == name:
            bot.send_message(message.chat.id, f"Your next lesson is at: {timetable} good luck!")
            found = True
            break
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
        student = row[3]
        group = row[1]
        if student == name:
            bot.send_message(message.chat.id, f"You're in group: {group}intresting<:0")
            found = True
            break
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
        student = row[3]
        lesson = row[0]
        if student == name:
            bot.send_message(message.chat.id, f"You're in class: {lesson} great choice!")
            found = True
            break
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
        student = row[3]
        lesson = row[0]
        timetable = row[2]
        group = row[1]
        if student == name:
            bot.send_message(message.chat.id, f"All info: {student}, {lesson}, {timetable}, {group} wow thats a lot!")
            found = True
            break
    if not found:
        bot.send_message(message.chat.id, "Sorry, idk who you are:(((((")
bot.infinity_polling()