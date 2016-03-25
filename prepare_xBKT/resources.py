# commonly used functions

# create an object to read 
def define_resource(quiz_type, quiz_attempt):
  quiz_attempt = str(quiz_attempt)
  quiz_resource = []
  if quiz_type  == 'QuizEngine::PreQuiz':
    quiz_resource = '0'
  elif quiz_attempt == '1':
    quiz_resource = '1'
  elif quiz_attempt == '2':
    quiz_resource = '2'
  else:
    quiz_resource = '3'
  return quiz_resource
  

def create_answer_array_for_attempt(answers, questionid_array):
  answer_array =[0 for q in questionid_array]
  questions = answers.keys()
  q_indx = [questionid_array.index(q) for q in questions]
  for q in q_indx: 
    answer_array[q] = int(answers[questionid_array[q]]) + 1
  return answer_array

def create_or_append_mat(answer_array, student_mat):
  answer_mat = np.matrix(answer_array)
  student_mat = np.r_[student_mat, answer_mat]
  return student_mat

def append_resource_by_attempt(resources, attempt):
  resources.append(int(attempt)) 
  return resources
