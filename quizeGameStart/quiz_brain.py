
class QuizBrain:

    def __init__(self,q_list):
        self.question_num=0
        self.question_list=q_list
        self.score=0


    def still_has_question(self):
        if self.question_num>=len(self.question_list):
            return False
        else:
            return True


    def next_question(self):
        current_quetion = self.question_list[self.question_num]
        self.question_num +=1
        u_ans = input(f"Q.{self.question_num}: {current_quetion.q_text} (True/False): ")
        # print(current_quetion.q_answer)
        self.check_ans(u_ans,current_quetion.q_answer)


    def check_ans(self,u_ans,right_ans):
        if right_ans == u_ans:
            self.score +=1
            print("You got it right!")
            print(f"Answer is {right_ans}")
            print(f"Score {self.score}/{self.question_num}")
        else:
            print("You got it wrong!")
            print(f"Correct answer is {right_ans}")
            print(f"Score {self.score}/{self.question_num}")

