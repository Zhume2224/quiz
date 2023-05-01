from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.quiz import Quiz

import repositories.user_repository as user_repo
import repositories.quiz_repository as quiz_repo

tasks_blueprint = Blueprint("scores", __name__)

@tasks_blueprint.route("/")
def tasks():
    users = user_repo.select_all() 
    quizzes=quiz_repo.select_by_user_id()
    return render_template("scores.jinja", all_users = users,quzzes=quizzes)