class Question:
    def __init__(self, txt, ans):
        self.question = txt
        self.answer = ans

class QuizBrain:
    def __init__(self, q_lst):
        self.score = 0
        self.question_number = 0
        self.question_lst = q_lst

    def still_has_question(self):
        return self.question_number < len(self.question_lst)
    
    def next_question(self):
        current_question = self.question_lst[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question}. (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got right!")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print()