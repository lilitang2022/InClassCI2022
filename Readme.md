# Function details  and how they work

## Motivation
We want to create a quiz apps for the authoized  student to test their understanding on the material before taking the actual exam. This application will ask user for the subject(Data533, Data541, Data530) and difficulty (easy, normal, hard, all(default)) that they want to be quized on. And validated their answer by giving feedback to them after every question. Finally the quiz apps will calculate a total marks after finishing all the question in order for them to keep track on their understanding on a specific topic. The application also allows teacher to access the quiz to see what question is the student being ask and for error checking purpose.
## Package1
This package will include the personal information input,output and checking. Also, we will divide it into two categories, student and teacher.
### Module 1
In Module 1, we will set functions about **information-input**, such as name, ID. If a student, users need to input their major and degree; if a teacher, users need to input their research direction and teaching length.
- def group():
- def name():
- def ID():
- def major():   
- def research():
### Module 2
In Module 2, we will set functions about **information-output**, we use the **inheritance** in this module. The Group will show the common information: name and ID. Inside the Group, there are Student (show additional information about major and degree) and Teacher (show additional information about research and length)
- class Group: 
- class Student(Group): 
- class Teacher(Group): 
### Module 3
Checking whether student or teacher is in the list, according to their ID, and checking whether the input of name is empty.
**Tips:As a testing example, now we only include two ID in the list,"12345" and "54321"**
-  def __init__(self):
-  def check_inlist(self, input):
-  def check_IsNull(self):


## Package2
This sub-package is all about processing question database and contain all the necessary checking function for the question and answer when user input in the quiz apps. This Sub-Package include 3 Module, **Checking**(the brain of the quiz apps), **Question**(for processing database question) and **Course**(appending defaulty to the  database question)
### Module 1
This Module contain ```class Checking: ```, which is the brain of the quizzing apps, it contain all the necessary checking function such as:
- isEmpty(self) - checking if there is more question to the question set. If there is, run function next_question() to prompt the user with new question and ask for their input.
- next_question(self) - prompt the user with new question and ask for their input and validate user answer using check_answer().
- check_answer(self, user_answer, correct_answer) - checking if the user input matched the database answer and if not prompt the user with the correct anser.
- check_score(self) - checking user score.

### Module 2
This Module contain ```class Question(Checking):```,which is inherited from Checking class, this class only have one function: 
-  __init__ (self, q_text, q_answer, q_diff) - process database’s question and allocate them into question, anser and difficulty.


### Module 3
This Module contain ```Course(Question,Checking):``` which is inherited from Checking class and Question class, this module are for appending database’s questions, answer into separate array with different difficulty for the other class to access based on user inputs in the future. this class only have 4 function: 
- append_text(self,question) - for appending database’s question in to its own question array
- append_answer(self,question) - for appending database’s answer in to its own answer array
- append_difficulty(self,question) - for appending database’s difficultyin to its own difficulty array
- append_courseq(self) - for appending database’s question, answer according to the difficulty into 4 different question set array for user to access it after knowing the user difficulty that he/she want to be quiz on.














