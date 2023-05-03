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
    users=user_repo.select_all()
    quizzes = quiz_repo.select_all()
    return render_template("quizzes.jinja", quizzes=quizzes,users=users)



@quiz_blueprint.route("/quizzes/<id>")
def get_quizzes_for_user(id):
    user=user_repo.select_by_id(id)
    quizzes = quiz_repo.select_quizzes_not_assigned_to_user(id)
    return render_template("take_quiz.jinja", quizzes=quizzes,user=user)


@quiz_blueprint.route("/quizzes/check", methods=['POST'])
def check_answer():
    user_id=request.form['user_id']
    # user=user_repo.select_by_id(user_id)

    quiz_id=request.form['quiz_id']
    quiz=quiz_repo.select_by_id(quiz_id)
    level=quiz.level

    answer_input=request.form['option']
    correct_answer=quiz_repo.select_correct_answer_by_id(quiz_id)
    
    if answer_input==correct_answer:
        user_repo.update_score_by_level(user_id,level)
    else:pass

    return redirect('/quizzes/' + user_id)





# @quiz_blueprint.route("/quizzes/<id>", methods=['POST'])
# def get_quiz(id):
#     users=user_repo.select_all()
#     # user_id_input is the user selected by client
#     user_id_input=request.form['user.id']

#     # user_on_web=user_repo.select_by_id(user_id_input)

#     quizzes=quiz_repo.select_quizzes_not_assigned_to_user(user_id_input)
#     return render_template("quizzes.jinja", users=users, quizzes=quizzes)









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
    
