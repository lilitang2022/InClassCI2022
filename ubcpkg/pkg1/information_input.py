def group():
        g=input("Are you a student or a teacher?")
        return g
    
def name():
        n=input("What's your name?")
        return n
    
def ID():   
     try:
        I=int(input("What's your ID? "))
        return I
     except ValueError:
        print("Please input a number")

# a student
def major():   
        n=input("What's your major?(optional)")
        return n
def degree():
        n=input("Are you an undergraduate or postgraduate?(optional)")
        return n
# a teacher    
def research():
        n=input("what is your research direction?(optional)")
        return n
    
def length():
        n=input("How many years since be a tearcher?(optional)")
        return n

