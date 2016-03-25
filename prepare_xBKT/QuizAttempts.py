from QuizResult import *

class QuizAttempts:

  def __init__(self):
    # self.student_id = student_id
    self.quiz_results =  {}

  def add_quiz_result(self, attempt, quiz_results):
    self.quiz_results[attempt] = quiz_results 

  def first_or_create(self, attempt):
    if attempt in self.quiz_results.keys():
      self.quiz_results[attempt]
    else:
      self.quiz_results[attempt] = QuizResult()
    return self.quiz_results[attempt]


  