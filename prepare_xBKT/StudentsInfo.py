from QuizAttempts import *

class StudentsInfo:

  def __init__(self):
    self.quiz_attempts_for_all_students = {}

  def add_quiz_attempt(self, student_id, quiz_attempts):
    self.quiz_attempts_for_all_students[student_id] = quiz_attempts 

  def first_or_create(self, student_id):
    if student_id in self.quiz_attempts_for_all_students.keys():
      self.quiz_attempts_for_all_students[student_id]
    else:
      self.quiz_attempts_for_all_students[student_id] = QuizAttempts()
    return self.quiz_attempts_for_all_students[student_id]
  