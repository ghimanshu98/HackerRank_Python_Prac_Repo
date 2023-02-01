# Using '+' operator to add two objects anf create new object

class Student:
    def __init__(self, m1, m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(a, b):
        m1 = a.m1 + b.m1
        m2 = a.m2 + b.m2
        return Student(m1, m2)

    def get(self):
        print('m1 : {} , m2 : {}'.format(self.m1, self.m2))

s1 = Student(10, 20)
s2 = Student(40, 30)
s3 = s1+s2

s1.get()
s2.get()
s3.get()
        
