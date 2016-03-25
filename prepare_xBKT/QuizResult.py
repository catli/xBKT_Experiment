class QuizResult:

  def __init__(self):
    self.answers = { }

  def add_answer(self, question_id, correct):
    self.answers[question_id] = correct

