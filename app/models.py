from .db import db
from werkzeug.security import check_password_hash


class Lesson(db.Model):

    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    time = db.Column(db.Time, nullable=False)
    room = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "time": self.time.strftime("%H:%M"),
            "room": self.room
        }


class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    absences = db.Column(db.Integer, default=0)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
