import unittest
from unittest.mock import patch
from repositories.quiz_repository import select_correct_answer_by_id

class TestQuiz(unittest.TestCase):
    @patch('repositories.quiz_repository.run_sql')
    def test_quiz(self, mock_run_sql):
        # run_sql should return {'correct_answer': 'Unicorn'}
        mock_run_sql.return_value = [{'correct_answer': 'Unicorn'}]
        # call the function to be tested
        result = select_correct_answer_by_id(29)

        self.assertEqual('Unicorn', result)


# use @patch from unittest.mock to mock the run_sql() function. We configure the mock to return a specific result, which is a dictionary with 'correct_answer' set to 'Unicorn'. By doing so, we have control over the expected response of the database query, making the test self-contained.

#  test doesn't rely on the actual database and will consistently pass as long as the function under test behaves correctly.