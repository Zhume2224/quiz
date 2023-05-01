from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.user import User
from models.quiz import Quiz
from models.answer import Answer

import repositories.user_repository as user_repo
import repositories.quiz_repository as quiz_repo
import repositories.answer_repository as answer_repo

scores_blueprint = Blueprint("scores", __name__)

@scores_blueprint.route("/")
def scores():
    users = user_repo.select_all()
    return render_template("scores.jinja", users = users)