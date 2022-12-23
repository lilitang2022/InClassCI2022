from pkg.pkg2 import Question as Q
from pkg.pkg2 import Checking as C

class Course(Q.Question,C.Checking):
    def __init__(self,question_data,input_diff,usr):
        self.course_q = []
        self.ez_course_q = []
        self.hard_course_q = []
        self.normal_course_q = []
        self.question_data = question_data
        self.inputdiff = input_diff
        self.usr = usr
        self.append_courseq()
        
        if self.inputdiff == "easy":
                C.Checking.__init__(self,self.ez_course_q,self.usr)
        elif self.inputdiff == "normal":
                C.Checking.__init__(self,self.normal_course_q,self.usr)
        elif self.inputdiff == "hard":
                C.Checking.__init__(self,self.hard_course_q,self.usr)
        else:
                C.Checking.__init__(self,self.course_q,self.usr)
            
        
    def append_text(self,question):
        self.question_text = question["question"]
        return question["question"]
            
    def append_answer(self,question):
        self.question_answer = question["correct_answer"]
        return question["correct_answer"]
            
    def append_difficulty(self,question):
        self.question_difficulty = question["difficulty"]
        return question["difficulty"]
    
            
    def append_courseq(self):
        for question in self.question_data:
            self.append_text(question)
            self.append_answer(question)
            self.append_difficulty(question)
            new_question = Q.Question(self.question_text, self.question_answer,self.question_difficulty)
           
            self.course_q.append(new_question)
            
            if self.question_difficulty == "easy":
                new_question = Q.Question(self.question_text, self.question_answer,self.question_difficulty)
                self.ez_course_q.append(new_question)
            elif self.question_difficulty == "normal":
                new_question = Q.Question(self.question_text, self.question_answer,self.question_difficulty)
                self.normal_course_q.append(new_question)
            elif self.question_difficulty == "hard":
                new_question = Q.Question(self.question_text, self.question_answer,self.question_difficulty)
                self.hard_course_q.append(new_question)
                