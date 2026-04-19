import sqlite3


def create_table():
    con = sqlite3.connect("school.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS school(lesson TEXT, side TEXT, timetable TEXT, student TEXT)"
    )
    con.commit()
    con.close()


def create_log(lesson, side, timetable, student):
    con = sqlite3.connect("school.db")
    cur = con.cursor()
    cur.execute(
        "INSERT INTO school(lesson, side, timetable, student) VALUES (?, ?, ?, ?)",
        (lesson, side, timetable, student),
    )
    con.commit()
    con.close()


def get_all_data():
    con = sqlite3.connect("school.db")
    cur = con.cursor()
    cur.execute("SELECT lesson, side, timetable, student FROM school")
    rows = cur.fetchall()
    con.close()
    return rows
