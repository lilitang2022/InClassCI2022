import unittest
from pkg.pkg1 import information_input as ii
from pkg.pkg1 import information_output as io
from pkg.pkg1 import information_check as ic
from pkg.pkg2 import Checking as ch
from pkg.pkg2 import Course as co
from pkg.pkg2 import Question as qu

class Test_output(unittest.TestCase):
    
    def setUp(self): 
        print('Set Up')
        self.student_name= 'lily'
        self.student_ID= 9130
        self.student_major='MDS'
        self.student_degree='Post'
        self.teacher_name= 'John'
        self.teacher_ID= 7788
        self.teachr_research='maching learning'
        self.teacher_length=5
        
    def tearDown(self):
        print('Tear Down')
        
    def test_student(self):
        p1= io.Student(self.student_name,self.student_ID,self.student_major,self.student_degree)
        p2 = io.Group(self.student_name,self.student_ID)
    
        self.assertEqual(p1.major,self.student_major)
        self.assertEqual(p1.degree,self.student_degree)
        self.assertEqual(p2.name,self.student_name)
        self.assertEqual(p2.ID,self.student_ID)
    
    def test_teacher(self):
        p3= io.Teacher(self.teacher_name,self.teacher_ID,self.teachr_research,self.teacher_length)
        p4 = io.Group(self.teacher_name,self.teacher_ID)
    
        self.assertEqual(p3.research,self.teachr_research)
        self.assertEqual(p3.length,self.teacher_length)
        self.assertEqual(p4.name,self.teacher_name)
        self.assertEqual(p4.ID,self.teacher_ID)
        
class Test_check(unittest.TestCase):
    
    def setUp(self): 
        print('1')
        self.right_name = 'lily'
        self.right1_name = 'Justin'
        self.right2_name = 'Travis'
        self.wrong_name = ''
        self.right_id = "12345"
        self.right2_id = "54321"
        self.wrong_id = "36345"
        self.wrong2_id = ""
                
    def tearDown(self):
        print('2')
        
    def test_check_inlist(self): #function
        right = ic.Info_Check(self.right_name,self.right_id)
        wrong = ic.Info_Check(self.wrong_name,self.wrong_id)
        right2 = ic.Info_Check(self.right2_id,self.right_id)
        wrong2 = ic.Info_Check(self.wrong_name,self.wrong_id)
        
        self.assertTrue(right.check_inlist())
        self.assertFalse(wrong.check_inlist())
        self.assertTrue(right2.check_inlist())
        self.assertFalse(wrong2.check_inlist())
              
        
    def test_check_IsNull(self):
        right = ic.Info_Check(self.right_name,self.right_id)
        wrong = ic.Info_Check(self.wrong_name,self.right_id)
        right1 = ic.Info_Check(self.right1_name,self.right_id)
        right2 = ic.Info_Check(self.right2_name,self.right_id)
        
        self.assertFalse(right.check_IsNull())
        self.assertTrue(wrong.check_IsNull())
        self.assertFalse(right1.check_IsNull())
        self.assertFalse(right2.check_IsNull())          
        
unittest.main()
