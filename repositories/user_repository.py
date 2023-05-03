from models.quiz import Quiz
from models.user import User
from db.run_sql import run_sql
import logging

def save(user):
    sql = 'INSERT INTO users(name, score) VALUES (%s, %s) RETURNING id'
    values = [user.name, user.score]
    result = run_sql(sql, values)
    user.id = result[0]['id']
    return user
    
# def delete_user_by_id(id):
#     sql = 'DELETE FROM users WHERE id=%s'
#     values = [id]
#     run_sql(sql, values)


def delete_user_by_id(id):
    # Replace user_id with admin_id in quizzes table
    sql_update_quiz = 'UPDATE quizzes SET user_id = %s WHERE user_id = %s'
    values = [7, id]
    run_sql(sql_update_quiz, values)

    # Delete user from users table
    sql_delete_user = 'DELETE FROM users WHERE id = %s'
    values = [id]
    run_sql(sql_delete_user, values)




# def delete_user_by_id(user_id):
#     try:
#         # disassociate quizzes from user
#         sql = 'UPDATE quizzes SET user_id = NULL WHERE user_id = %s'
#         values = [user_id]
#         run_sql(sql, values)

#         # delete user
#         # sql = 'DELETE FROM users WHERE id = %s'
#         # values = [user_id]
#         # run_sql(sql, values)
#     except Exception as e:
#         logging.error(f'Error deleting user: {e}')
#         raise e





def select_by_id(id):
    user = None
    sql = 'SELECT * FROM users WHERE id=%s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        user = User(result['name'], result['score'], result['id'])
    return user

def select_all():
    users = []
    sql = 'SELECT * FROM users'
    results = run_sql(sql)

    for row in results:
        user = User(row['name'], row['score'], row['id'])
        users.append(user)

    return users

def update_score_to_0():
    sql = "UPDATE users SET score = 0 WHERE score IS NULL"
    run_sql(sql)

def update_score_by_level(user_id, level):
    sql = "UPDATE users SET score = score + %s WHERE id = %s"
    values = [level, user_id]
    run_sql(sql, values)
