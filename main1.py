import data1
import telebot 
data1.create_table()

lesson = input('enter the lesson your student will have: ')
side = input('enter which side the student is on: ')
timetable = input('enter the timetable of the class: ')
student = input("enter student's name: ")

data1.create_log(lesson, side, timetable, student)

print('logged in')