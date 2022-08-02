class QuizBrain:
    def __init__(self, q_list, q_numbers):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.number_of_questions = q_numbers

    def next_question(self):
        for i in range(self.number_of_questions):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?:")
            self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("great guess!!")
            self.score += 1
        else:
            print("That is not correct")
        print(f"You got {self.score} out of {self.question_number} ")
        print("\n")








