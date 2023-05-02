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


@quiz_blueprint.route("/quizzes/<id>", methods=['POST'])
def get_quizzes(id):
    users=user_repo.select_all()
    quizzes=quiz_repo.select_quizzes_not_assigned_to_user(id)
    return render_template("quizzes.jinja", users=users, quizzes=quizzes)




# @quiz_blueprint.route("/quizzes", methods=['POST'])
# def check_answer():
#     input_answer=request.form['option']
#     quiz_id=request.form['quiz_id']

#     quiz=quiz_repo.select_by_id(quiz_id)
#     correct_answer=quiz_repo.select_correct_answer_by_id(quiz_id)
#     if input_answer==correct_answer:
#         user_repo.update_score_by_level(  ,quiz.level)
        # parametor1: user who is ansering
        # parametor2: quiz.level




        # this part should increase user's score
        # user's score==0 by default
        # user's score should increse by 







    # quiz=Quiz(result['quiz'],result['opt1'],result['opt2'],result['opt3'],result['correct_answer'],)



    # find quiz in database from form ['quiz_id']
    # compare form ['option'] to correct answer
    # if the option matches the correct answer in the database then Correct = True
    # else correct = false
    # create the answer class and save into database
    # user_answer1=request.form['opt1']
    # user_answer2=request.form['opt2']
    # user_answer3=request.form['opt3']
    
