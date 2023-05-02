from models.quiz import Quiz
from models.user import User
from models.answer import Answer

import repositories.quiz_repository as quiz_repo
import repositories.user_repository as user_repo
import repositories.answer_repository as answer_repo

# user1=User('Archie')
# result1=user_repo.save(user1)
# print(result1.__dict__)

# result=user_repo.select_all()
# for row in result:
#    print(row.__dict__)

# above has tested save,delete,select,select_all functions on user_repo


# print(user_repo.select_by_id(6).__dict__)
# ------------------devide----------------


# user1=User('Jack',6)
# quiz1=Quiz('which bird eats elephant?','eagle',
#            'sparrow','ladybird','ladybird',1,user1)
# quiz_repo.save(quiz1)

# results=quiz_repo.select_by_id(1)
# for row in results:
# print(results.__dict__) 

# results=quiz_repo.select_by_user_id(1)
# for row in results:
#     print(row.__dict__)


# results=quiz_repo.select_by_user_id(1)
# for row in results:
#     print(row.__dict__)

# # quiz_repo.delete_by_id(5)
# user1=User('Greg',1)
# # user1=user_repo.select_by_id(1)
# quiz=Quiz('who loves red','zhu','archie','ken',
#          'zhu',1, user1, 1)
# quiz_repo.update(quiz)


# users = user_repo.select_all()
# for user in users:
#     print(user.__dict__)

# results=answer_repo.select_false_quizzes(1)
# for quiz in results:
#     print(quiz.__dict__)

# results=answer_repo.select_user_by_user_id(1)
# print(results.__dict__)


# user_repo.update_score_by_level(1,2)
# user_repo.update_score_by_level(1,2)

