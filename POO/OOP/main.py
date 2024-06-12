from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# Iterate through a list of dictionaries
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    # add question to question bank
    question_bank.append(new_question)

print(question_bank[0].answer)
print(question_bank[0].text)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")