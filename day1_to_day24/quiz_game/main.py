from quiz_brain import Question, QuizBrain
from data import questions_database

question_bank = []
for question in questions_database:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



        