from flask import Flask, render_template
from controllers.quiz_controller import quizzes_blueprint



app = Flask(__name__)

app.register_blueprint(quizzes_blueprint)

@app.route('/')
def home():
    return render_template('scores.jinja')

if __name__ == '__main__':
    app.run(debug=True)
