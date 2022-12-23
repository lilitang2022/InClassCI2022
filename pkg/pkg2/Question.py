from pkg.pkg2 import Checking as C

class Question(C.Checking):
    def __init__(self, q_text, q_answer, q_diff):
        self.text = q_text
        self.answer = q_answer
        self.diff = q_diff
    