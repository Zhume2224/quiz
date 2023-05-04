from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.quiz import Quiz
from models.answer import Answer

import repositories.user_repository as user_repo
import repositories.quiz_repository as quiz_repo
import repositories.answer_repository as answer_repo


addmore_blueprint = Blueprint("addmore", __name__)
@addmore_blueprint.route("/addmore", methods=['Get'])
def show_addmore_page():
    users=user_repo.select_all()
    quizzes=quiz_repo.select_all()
    return render_template('addmore.jinja',users=users,quizzes=quizzes)


@addmore_blueprint.route("/addmore/add_user", methods=['POST'])
def add_user():
    user_name=request.form['user_name']
    user_score=request.form['user_score']
    user=User(user_name,user_score)
    user_repo.save(user)
    return redirect ("/")

@addmore_blueprint.route("/addmore/delete_user", methods=['POST'])
def delete_user():
    id = request.form['user_id']
    user_repo.delete_user_by_id(id)
    return redirect ("/")

@addmore_blueprint.route("/addmore/add_quizzes", methods=['POST'])
def add_quiz():
    user_id=request.form['admin_id']
    user=user_repo.select_by_id(user_id)
    quiz=request.form['quiz']
    opt1=request.form['opt1']
    opt2=request.form['opt2']
    opt3=request.form['opt3']
    correct_answer=request.form['correct_answer']
    level=request.form['level']
    quiz_to_save=Quiz(quiz,opt1,opt2,opt3,correct_answer,level,user)
    quiz_repo.save(quiz_to_save)

    return redirect ("/addmore")

# show all: 
@addmore_blueprint.route("/addmore/<id>")
def show_quiz(id):
   quiz=quiz_repo.select_by_id(id)
   users=user_repo.select_all()
   return render_template('edit.jinja',quiz=quiz,users=users)
     
# show individual quiz
@addmore_blueprint.route("/addmore/<id>/edit", methods=['POST'])
def edit_quiz(id):
    user_id=request.form['admin_id']
    user=user_repo.select_by_id(user_id)
    quiz=request.form['quiz']
    opt1=request.form['opt1']
    opt2=request.form['opt2']
    opt3=request.form['opt3']
    correct_answer=request.form['correct_answer']
    level=request.form['level']
    quiz_to_update=Quiz(quiz,opt1,opt2,opt3,correct_answer,level,user,id)
    quiz_repo.update(quiz_to_update)

    return redirect("/quizzes")




# @addmore_blueprint.route("/addmore/<id>", methods=['POST'])
# def update_selected_quiz():
#    quizzes=quiz_repo.select_all()
#    return render_template('edit.jinja',quizzes=quizzes)