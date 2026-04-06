from datetime import time
from werkzeug.security import generate_password_hash
from .db import db
from .models import Lesson, Student


def init_db():

    db.create_all()

    if Lesson.query.first():
        return

    lessons = [
        Lesson(name="Юриспруденция", time=time(15, 0), room="АД420"),
        Lesson(name="Философия", time=time(9, 0), room="3450"),
        Lesson(name="Высшая математика", time=time(17, 40), room="Б407"),
        Lesson(name="Физическая культура", time=time(10, 0), room="Спортзал №2"),
    ]

    students = [
        Student(
            login="yvmelni",
            password_hash=generate_password_hash("oijB64"),
            absences=0
        ),
        Student(
            login="azakhar",
            password_hash=generate_password_hash("KLJH1"),
            absences=13
        ),
        Student(
            login="ashamrai",
            password_hash=generate_password_hash("juhYGd3"),
            absences=4
        ),
    ]

    db.session.add_all(lessons)
    db.session.add_all(students)
    db.session.commit()
