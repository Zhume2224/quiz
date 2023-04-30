from models.quiz import Quiz
from models.user import User
from db.run_sql import run_sql

def save(user):
    sql='INSERT INTO users(name) VALUES (%s) RETURNING id'
    values=[user.name]
    result=run_sql(sql,values)
    user.id=result[0]['id']
    return user
    
def delete_by_id(id):
    sql='DELETE FROM users WHERE id=%s'
    values=[id]
    run_sql(sql,values)

def select_by_id(id):
    user=None
    sql='SELECT * FROM users WHERE id=%s'
    values=[id]
    results=run_sql(sql,values)
    if results:
        result=results[0]
        user=User(result['name'],result['id'])
    return user

def select_all():
    users=[]
    sql='SELECT * FROM users'
    results=run_sql(sql)

    for row in results:
        user=User(row['name'],row['id'])
        users.append(user)

    return users



