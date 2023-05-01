from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.quiz import Quiz
from models.answer import Answer

import repositories.user_repository as user_repo
import repositories.quiz_repository as quiz_repo
import repositories.answer_repository as answer_repo


quiz_blueprint = Blueprint("quizzes", __name__)

@quiz_blueprint.route("/quizzes")
def get_quizzes():
    quizzes = quiz_repo.select_all()
    return render_template("quizzes.jinja", quizzes=quizzes)



@quiz_blueprint.route("/quizzes", methods=['POST'])
def check_answer():
    # find quiz in database from form ['quiz_id']
    # compare form ['option'] to correct answer
    # if the option matches the correct answer in the database then Correct = True
    # else correct = false
    # create the answer class and save into database
    user_answer1=request.form['opt1']
    user_answer2=request.form['opt2']
    user_answer3=request.form['opt3']
    
