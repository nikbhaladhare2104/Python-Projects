from question_model import Question
from data import question_data, question
from quiz_brain import QuizBrain

print("\n")
# For question data


# question_bank = []
# for item in question:
#     text = item["question"]
#     ans = item["correct_answer"]
#     q = Question(text, ans)
#     question_bank.append(q)



question_bank = []
for item in question_data:
    text = item["text"]
    ans = item["answer"]
    q = Question(text, ans)
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_que()
    print("\n")
print("you completed the quiz!")
print(f"your final score is: {quiz.score}/{len(quiz.que_list)}")
print("\n")
