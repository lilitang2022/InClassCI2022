import unittest
from pkg.pkg1 import information_input as ii
from pkg.pkg1 import information_output as io
from pkg.pkg1 import information_check as ic
from pkg.pkg2 import Checking as ch
from pkg.pkg2 import Course as co
from pkg.pkg2 import Question as qu

def addition(num1, num2):
    return num1 + num2

# Checking.py
import unittest
class TestCheck(unittest.TestCase):
    def setUp(self): # Setting up for the test 
        print('Set Up')
        self.teacher_have_data = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "teacher")
        self.teacher_have_no_data = co.Course([]," ", "teacher")
        self.student_have_data = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "student")
        self.student_have_no_data = co.Course([]," ", "student")
        
    def tearDown(self):
        print('Tear Down')
    
    def test_isEmpty(self):
        self.assertTrue(self.teacher_have_data.isEmpty())
        self.assertFalse(self.teacher_have_no_data.isEmpty())
        self.assertTrue(self.student_have_data.isEmpty())
        self.assertFalse(self.student_have_no_data.isEmpty())
        
    def test_check_answer(self):
        self.assertTrue(self.teacher_have_no_data.check_answer("3","3"))
        self.assertFalse(self.teacher_have_no_data.check_answer("3","0"))
        self.assertTrue(self.student_have_data.check_answer("3","3"))
        self.assertFalse(self.student_have_data.check_answer("3","0"))

        
# Course.py
class TestCourse(unittest.TestCase):
    def setUp(self): # Setting up for the test 
        print('Set Up')
        self.correct_question = "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n"
        self.data1 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]
        self.data2 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "4","difficulty": "normal"}]
        self.data3 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "5","difficulty": "hard"}]
        self.data4 = [{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "6","difficulty": ""}]
        self.teacher_have_data1 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "3","difficulty": "easy"}]," ", "teacher")
        self.teacher_have_data2 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "4","difficulty": "normal"}]," ", "teacher")
        self.teacher_have_data3 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "5","difficulty": "hard"}]," ", "teacher")
        self.teacher_have_data4 = co.Course([{ "question": "How many of the following statements are TRUE?(Answer in Number) \n1) Git is a is distributed version control system \n2) Git is designed to support parallel development \n3) Git is a web-based repository Service \n4) Git doesn’t require a server \n","correct_answer": "6","difficulty": ""}]," ", "teacher")
    
    def tearDown(self):
        print('Tear Down')
        
    def test_append_text(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_text(question), self.correct_question)
            
    def test_append_answer(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_answer(question), "3")
        for question in self.data2:
            self.assertEqual(self.teacher_have_data2.append_answer(question), "4")
        for question in self.data3:
            self.assertEqual(self.teacher_have_data3.append_answer(question), "5")
        for question in self.data4:
            self.assertEqual(self.teacher_have_data4.append_answer(question), "6")

    def test_append_difficulty(self):
        for question in self.data1:
            self.assertEqual(self.teacher_have_data1.append_difficulty(question), "easy")
        for question in self.data2:
            self.assertEqual(self.teacher_have_data2.append_difficulty(question), "normal")
        for question in self.data3:
            self.assertEqual(self.teacher_have_data3.append_difficulty(question), "hard")
        for question in self.data4:
            self.assertEqual(self.teacher_have_data4.append_difficulty(question), "")
            
unittest.main()

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCheck))
    suite.addTest(unittest.makeSuite(TestCourse))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()