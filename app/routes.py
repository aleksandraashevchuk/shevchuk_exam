from flask import Blueprint, jsonify, request
from .models import Lesson, Student

api = Blueprint("api", __name__)


@api.route("/lessons", methods=["GET"])
def get_lessons():

    lessons = Lesson.query.order_by(Lesson.time).all()

    return jsonify([l.to_dict() for l in lessons])


@api.route("/attendance", methods=["POST"])
def attendance():

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON required"}), 400

    login = data.get("login")
    password = data.get("password")

    if not login or not password:
        return jsonify({"error": "login and password required"}), 400

    student = Student.query.filter_by(login=login).first()

    if not student or not student.check_password(password):
        return jsonify({"error": "invalid credentials"}), 401

    return jsonify({
        "login": student.login,
        "absences": student.absences
    })
