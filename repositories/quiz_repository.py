from db.run_sql import run_sql

from models.quiz import Quiz
from models.user import User

import repositories.user_repository as user_repo

# save quiz
def save(quiz):
    sql='INSERT INTO quizzes(quiz,opt1,opt2,opt3,correct_answer,level,user_id) VALUES(%s,%s,%s,%s,%s,%s,%s) RETURNING *'
    values=[quiz.quiz, quiz.opt1,quiz.opt2,quiz.opt3,quiz.correct_answer,quiz.level,quiz.user.id]
    result=run_sql(sql,values)
    quiz.id=result[0]['id']
    return quiz

# get quiz all
def select_all():
    quizzes=[]
    sql='SELECT * FROM quizzes'
    results=run_sql(sql)

    for row in results:
        user=user_repo.select_by_id(row['user_id'])
        quiz=Quiz(row['quiz'],row['opt1'],row['opt2'],row['opt3'],row['correct_answer'],row['level'],user,row['id'] )
        quizzes.append(quiz)
    return quizzes

# get quiz by id
def select_by_id(id):
    sql='SELECT * FROM quizzes WHERE id=%s'
    values=[id]
    results=run_sql(sql,values)

    result=results[0]
    user=user_repo.select_by_id(result['user_id'])
    quiz=Quiz(result['quiz'],result['opt1'],result['opt2'],result['opt3'],result['correct_answer'],result['level'],user,result['id'] )

    return quiz

# get quiz by user_id
def select_by_user_id(user_id):
    quizzes=[]
    sql='SELECT * FROM quizzes WHERE user_id=%s'
    values=[user_id]
    results=run_sql(sql,values)

    for result in results:
        user=user_repo.select_by_id(user_id)
        quiz=Quiz(result['quiz'],result['opt1'],result['opt2'],result['opt3'],result['correct_answer'],result['level'],user,result['id'] )
        quizzes.append(quiz)

    return quizzes

# get quiz by level
def select_by_user_id(level):
    quizzes=[]
    sql='SELECT * FROM quizzes WHERE level=%s'
    values=[level]
    results=run_sql(sql,values)

    for result in results:
        # user=user_repo.select_all()
        quiz=Quiz(result['quiz'],result['opt1'],result['opt2'],result['opt3'],result['correct_answer'],result['level'],result['user_id'],result['id'] )
        quizzes.append(quiz)

    return quizzes


# delete quiz by id
def delete_by_id(id):
    sql='DELETE  FROM quizzes WHERE id=%s'
    values=[id]
    run_sql(sql,values)

# delete all quizzes
def delete_all():
    sql='DELETE  FROM quizzes'
    run_sql(sql)

# update quiz
def update(quiz):
    sql = 'UPDATE quizzes SET quiz = %s, opt1 = %s, opt2 = %s, opt3 = %s, correct_answer = %s, level = %s, user_id = %s WHERE id = %s'
    values=[quiz.quiz,quiz.opt1, quiz.opt2,quiz.opt3,quiz.correct_answer,quiz.level,quiz.user.id,quiz.id]
    run_sql(sql, values)

# get correct answer by id
def select_correct_answer_by_id(id):
    sql = 'SELECT correct_answer FROM quizzes WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)
    if result:
        return result[0]['correct_answer']
    else:
        return None


def select_quizzes_not_assigned_to_user(user_id):
    quizzes = []
    sql = "SELECT * FROM quizzes WHERE user_id != %s;"
    values = [user_id]
    results = run_sql(sql, values)
    for row in results:
        quiz = Quiz(row['quiz'], row['opt1'], row['opt2'], row['opt3'], row['correct_answer'], row['level'], row['user_id'], row['id'])
        quizzes.append(quiz)
    return quizzes
