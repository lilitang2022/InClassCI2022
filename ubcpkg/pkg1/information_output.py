class Group: 
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
          
    def display(self):
        print('Name:{} ID:{} '.format(self.name, self.ID))


class Student(Group): 
    def __init__(self, name, ID, major, degree):
        Group.__init__(self, name, ID)
        self.major=major
        self.degree=degree
        
    def display(self):
        Group.display(self)
        print('Major: {} Degree: {}'.format(self.major, self.degree))

class Teacher(Group): 
    def __init__(self, name, ID, research, length):
        Group.__init__(self, name, ID)
        self.research=research
        self.length=length
        
    def display(self):
        Group.display(self)
        print('Research: {} Length: {}'.format(self.research, self.length))