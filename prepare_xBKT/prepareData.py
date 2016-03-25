# We use this to read the xBKT data 
import csv 
import pandas as pd
import os 
import numpy as np

from resources import *
from QuizResult import * 
from QuizAttempts import *
from StudentsInfo import *


# set the directory to read data from
questionpath = '/Users/cathleenli/Dropbox/Catris/xBKT/query_quest_data_xBKT_all.csv'
outputpath = '/Users/cathleenli/Dropbox/Catris/xBKT/'
standard_sel = 'K.RF.2.a'

# use csv reader to open and read file
f = open(questionpath) 
reader = csv.reader(f)

# store header 
header = next(reader)
# store column for key variables
standard_indx = header.index('lesson_standard')
student_indx = header.index('student_id')
question_indx = header.index('question_id')
correct_indx = header.index('correct')
quiz_type_indx = header.index('quiz_type')
quiz_att_indx = header.index('quiz_attempt')
sq_indx = header.index('student_quest_id')


# instantiate StudentsInfo
studentsinfo = StudentsInfo()

#find the unique questions for all 
questionid_array = []

# loop through each row
for row in reader:
  # filter the data by standard, if not equal than pass
  if row[standard_indx]!=standard_sel:
	  pass
  else:
  # else read in the csv file into hash map with the following hierarchy: 
  # students -> quiz step -> questions
    student_id = row[student_indx]
    question_id = row[question_indx]
    correct = row[correct_indx]
    # add question to array if not in there
    if not question_id in questionid_array: questionid_array.append( question_id ) 
    # define quiz resource 
    quiz_attempt = define_resource(row[quiz_type_indx], row[quiz_att_indx])
    # find or create the instance of quiz attempts for student
    quiz_attempts = studentsinfo.first_or_create(student_id)
    # find or create the instance of questions 
    quiz_questions = quiz_attempts.first_or_create(quiz_attempt)
    # define whether question id is correct
    quiz_questions.answers[question_id] = correct 
    # update quiz attempts
    quiz_attempts.add_quiz_result(quiz_attempt, quiz_questions)
    # update student info
    studentsinfo.add_quiz_attempt(student_id, quiz_attempts)


# write the hashmap to csv
studentinfo_mat = np.matrix([int(q) for q in questionid_array])
student_idx_array = []
student_idx = 1 
resources = []
lengths = []

for student_id in studentsinfo.quiz_attempts_for_all_students:
  quiz_attempts = studentsinfo.quiz_attempts_for_all_students[student_id]
  attempt_keys = sorted( quiz_attempts.quiz_results.keys() )
  if len(attempt_keys)>1:
    student_idx_array.append(student_idx)
    for attempt in attempt_keys:
      resources = append_resource_by_attempt(resources, attempt)
      student_idx+=1
      answers = quiz_attempts.quiz_results[attempt].answers
      answer_array = create_answer_array_for_attempt(answers, questionid_array)
      studentinfo_mat = create_or_append_mat(answer_array, studentinfo_mat)
    lengths.append( student_idx - student_idx_array[ len(student_idx_array) -1 ])


studentinfo_write = np.transpose( studentinfo_mat)
student_idx_write = np.matrix(student_idx_array)
resource_write = np.matrix(resources)
lengths_write = np.matrix(lengths)

np.savetxt(outputpath + 'xBKT_resources.csv', 
          resource_write, 
          delimiter= ',',
          newline='\n')

np.savetxt(outputpath + 'xBKT_student_matrix.csv', 
          studentinfo_write, 
          delimiter= ',',
          newline='\n')

np.savetxt(outputpath + 'xBKT_student_idx.csv',
          student_idx_write, 
          delimiter=',',
          newline='\n')

np.savetxt(outputpath + 'xBKT_length.csv',
          lengths_write, 
          delimiter=',',
          newline='\n')





