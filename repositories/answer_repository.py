from db.run_sql import run_sql

from models.quiz import Quiz
from models.user import User
from models.answer import Answer

import repositories.user_repository as user_repo
import repositories.quiz_repository as quiz_repo

# save answer
def save(answer):
    sql='INSERT INTO answers(user_id,quiz_id,correct) VALUES(%s,%s,%s) RETURNING *'
    values=[answer.user.id, answer.quiz.id, answer.correct]
    result=run_sql(sql,values)
    answer.id=result[0]['id']
    return answer


# get answer(true/false) by user_id
def select_by_user_id(user_id):
    answers=[]
    sql='SELECT * FROM answers WHERE user_id=%s'
    values=[user_id]
    results=run_sql(sql,values)

    for result in results:
        user=user_repo.select_by_id(user_id)
        quiz=quiz_repo.select_by_user_id(user_id)
        answer=Answer(user,quiz,result['id'] )
        answers.append(answer)

    return answers

# get all answers
def select_all():
    answers=[]
    sql='SELECT * FROM answers'
    results=run_sql(sql)

    for row in results:
        user=user_repo.select_by_id(row['user_id'])
        quiz=quiz_repo.select_by_user_id(row['user_id'])
        answer=Answer(user,quiz,row['id'] )
        answers.append(answer)
    return answers
# get user by user_id
def select_user_by_user_id(user_id):
    user=None
    sql='SELECT users.* FROM users JOIN answers ON users.id = answers.user_id WHERE answers.user_id = %s'
    values=[user_id]
    results=run_sql(sql,values)
    if results:
        result=results[0]
        user=User(result['name'],result['id'] )

    return user



# get questions where user doesnt answer right.
def select_false_quizzes(user_id):
    quizzes=[]
    sql='SELECT quizzes.* FROM quizzes JOIN answers ON quizzes.id = answers.quiz_id WHERE answers.user_id = %s AND answers.correct = false'
    values=[user_id]
    results=run_sql(sql,values)

    for result in results:
        user=user_repo.select_by_id(user_id)
        quiz=Quiz(result['quiz'],result['opt1'],result['opt2'],result['opt3'],result['correct_answer'],result['level'],user,result['id'])
        quizzes.append(quiz)

    return quizzes
        
                  
                  






# # get quiz_id by user_id and correct
# def select_quiz_by_user_id_correct(user,correct):
#     quizzes=[]
#     sql='SELECT * FROM answers WHERE user_id=%s AND correct=%s'
#     values=[user.id,True]
#     results=run_sql(sql,values)

#     for result in results:
#         user=user_repo.select_by_id(result['id'])




# def get_score_for_user(user or user_id):
#     pass
    # sql querey where id = user.id count all Correct = True
    # return total score for the user

    # sql querey which get all the quizes the user has answered correctly in list
    # loop the list and sum the "level" property
