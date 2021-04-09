from data import question_data
from question_model import Questions
from quiz_brain import QuizBrain
# from random import randrange

question_bank=[]
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_question = Questions(q_text=question_text,q_answer=question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("quiz has completed")
print(f"Final score {quiz.score} ")

# print(question_bank[1].q_text + question_bank[1].q_answer)
# QuizBrain.next_question(q_text=question_bank[1].q_text,q_ans=question_bank[1].q_answer)
# questions=1
# won=0
# while questions <=5:
#     num = randrange(0,len(question_data))
#     # print(question_data[num]["text"])
#     ans = input(question_data[num]["text"])
#
#     if question_data[num]["answer"] ==ans:
#         print("won")
#         won+=1
#     else:
#         print("Lost")
#     print(f"your score {won} / {questions}")
#     questions += 1
# print(f"your final score {won} / {questions-1}")