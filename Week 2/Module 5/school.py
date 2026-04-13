class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id
    
    def __repr__(self) -> str:
        return f'Student name: {self.name}, class: {self.current_class}, id: {self.id}'

class Teacher:
    def __init__(self,name,id,subject):
        self.name = name
        self.id = id
        self.subject = subject
    
    def __repr__(self):
        return f'The teacher\'s name: {self.name}, id: {self.id}, subject: {self.subject}'
    
class School:
    def __init__(self,name):
        self.name = name
        self.teacher = []
        self.student = []

    def add_teacher(self,name,subject):
        id = len(self.teacher) + 101
        teacher = Teacher(name,id,subject)
        self.teacher.append(teacher)

    def enroll(self,name,fee):
        if fee < 10000:
            print(f'You don\'t give valid fees.')
        else:
            id = len(self.student) + 1
            student = Student(name, 10,id)
            self.student.append(student)
            if fee == 10000:
                print('Thank You')
            elif fee > 10000:
                print(f'Wait, I will return extra {fee - 10000} Taka')
            

# # Student 
# pranto = Student('panto',15,315242055) 
# print(pranto)

# # Teacher
# hasnat = Teacher('Hasnat Hossain', 12345, 'Algo')
# print(hasnat)

scl = School('Vhondo High School')
scl.enroll('Abdullah',12000)    # Output: Wait, I will return extra 2000 Taka
scl.enroll('Tanvir',10000)      # Output: Thank You
scl.enroll('Pranto',1000)       # Output: You don't give valid fees.
scl.enroll('Farhan',10000)      # Output: Thank You
print(scl.student)              # Output: [Student name: Abdullah, class: 10, id: 1, 
                                          #Student name: Tanvir, class: 10, id: 2, 
                                          #Student name: Farhan, class: 10, id: 3]