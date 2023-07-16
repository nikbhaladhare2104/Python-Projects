class QuizBrain:
    def __init__(self, que_list):
        self.que_number = 0
        self.que_list = que_list
        self.score =0

    
    def still_has_question(self):
        return self.que_number < len(self.que_list)

    

    def next_que(self):
        que = self.que_list[self.que_number]
        self.que_number+=1
        guess  = input(f"Q.{self.que_number}: {que.text} (True/False)?: ")
        self.check_answer(guess, que.answer)


    def check_answer(self, guess, correct_answer):
        if guess.lower() == correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You are wrong.")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.que_number} ")



        
# Full answer
    # def next_que(self):
    #     n = len(self.que_list)
    #     score = 0
    #     while self.que_number<  n:
    #         que = self.que_list[self.que_number]
    #         guess  = input(f"Q.{self.que_number+1}: {que.text} (True/False)?: ")
    #         if guess.lower() == que.answer.lower():
    #             print("You got it right!")
    #             print(f"The correct answer was: {que.answer}")
    #             score+=1
    #             print(f"Your current score is: {score}/{self.que_number+1} ")


    #         self.que_number+=1
    #         print("\n")
    