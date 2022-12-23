class usr_notfound(Exception):
    def __init__(self):
        print("USER NOT FOUND (Teacher or Student)")
        
class Checking:

    def __init__(self, questions, usr):
        self.quesBank = questions
        self.usr = usr
        # self.usr_input = usr_input
        self.NumInQSet = len(questions)
        self.quesNum = 0
        self.score = 0
        self.ez_course_q = []
        self.hard_course_q = []
        self.normal_course_q = []
        
    def next_question(self):
        try:
            current_question = self.quesBank[self.quesNum]

            self.quesNum += 1


            if self.usr == 'teacher':
                print("Question " + str(self.quesNum)+ ". " + str(current_question.text))
                self.check_answer(current_question.answer, current_question.answer)
            elif self.usr == 'student':
                usr_input = input("Question " + str(self.quesNum)+ ". " + str(current_question.text))
                self.check_answer(usr_input.lower(), current_question.answer)
            else:
                raise usr_notfound
        except usr_notfound:
            pass
    
    def isEmpty(self):
        return self.quesNum < len(self.quesBank)

    def check_answer(self, user_answer, correct_answer):
        
        if user_answer.lower() == correct_answer:
            if self.usr == 'teacher':
                self.score += 1
                print("Correct answer is: " + str(correct_answer)+ "\n")
                return(True)
                
            else:
                self.score += 1
                print("Correct!!! \n \n \n")
                return(True)
                
        else:
            print("Wrong   :( \n \n \n")
            print("The correct answer is: " + str(correct_answer)+ "\n")
            return(False)
            
    def check_score(self):
        try:
            print("**************************************** ")
            print("**************************************** \n")
            print("Final score: " + str(self.score) + " out of " + str(self.quesNum) + ". \n")
            print("**************************************** ")
            print("**************************************** \n")
        except ValueError:
            print("ERROR Message: There is an Value error on the score")
        