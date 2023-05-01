from flask import Flask, render_template
from controllers.user_controller import scores_blueprint
from controllers.quiz_controller import quiz_blueprint
# from controllers.quiz_controller import quizzes_blueprint




app = Flask(__name__)

app.register_blueprint(scores_blueprint)
app.register_blueprint(quiz_blueprint)

@app.route('/')
def home():
    return render_template('scores.jinja')

if __name__ == '__main__':
    app.run(debug=True)
