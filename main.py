from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

number_of_questions = int(input("How many questions would you like?"))
quiz = QuizBrain(question_bank, number_of_questions)
quiz.next_question()

print("You've fished the quiz!!!")
print(f"You got a total of {quiz.score} out of {number_of_questions} ")