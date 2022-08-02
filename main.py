from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random

question_bank = []
# unused_questions = question_data
for x in range (1, len(question_data)):
    random_question = random.choice(question_data)
    del question_data[question_data.index(random_question)]
    question_text = random_question["question"]
    question_answer = random_question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

number_of_questions = int(input("How many questions would you like?"))
quiz = QuizBrain(question_bank, number_of_questions)
quiz.next_question()

print("You've fished the quiz!!!")
print(f"You got a total of {quiz.score} out of {number_of_questions} ")