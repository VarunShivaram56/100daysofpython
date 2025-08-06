from question_model import Question
from data import question_data
from quiz_brain import quiz_brain  

question_bank = []
for question in question_data:
    question_text=question['question']
    question_answer=question['correct_answer']
    explanation=question['explanation']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question) 

quiz=quiz_brain(question_bank)


while quiz.still_has_questions():
   quiz.next_question()
   print(f"The correct answer was {question_data[quiz.question_number - 1]['explanation']}.")

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
