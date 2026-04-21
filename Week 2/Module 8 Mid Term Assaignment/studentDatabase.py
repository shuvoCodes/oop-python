class StudentDatabase:
    student_list =[]

    @classmethod
    def add_student(cls,info):
        cls.student_list.append(info)

class Student:
    def __init__(self,student_id,name,department,is_enrolled = True):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self) 


    @classmethod
    def get_id(cls,id):
        for student in StudentDatabase.student_list:
            if student.__student_id == id:
                return True
                
        return False

    @classmethod
    def enroll_student(cls,id):
        for item in StudentDatabase.student_list:
            if item.__student_id == id:
                if item.__is_enrolled:
                    print('This Id Alrady Enrolled.')
                else:
                    item.__is_enrolled = True
                    print('Your Enroll Successfully Completed.')
    @classmethod
    def drop_student(cls,id):
        for item in StudentDatabase.student_list:
            if item.__student_id == id:
                if item.__is_enrolled:
                    item.__is_enrolled = False
                    print('This Id Successfully Droped')
                else:
                    print('This Id Alrady Droped')

    @classmethod
    def view_all_student(cls):
        for student in StudentDatabase.student_list:
            info = f'ID: {student.__student_id}, Name: {student.__name}, Department: {student.__department}, Enrolled: {student.__is_enrolled}'
            print(info)



Student(315242083, 'Abdullah', 'CSE')
Student(315242055, 'Pranto', 'CSE')
Student(315242084, 'Farhan', 'CSE')
Student(315242053, 'Tanvir', 'CSE')


while True:

    print('\n-----Student Management System-----\n')
    
    print('1. View All Student')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')

    choos = int(input('Enter Your Selected Number : '))
    
    if choos == 1:                                             # For 1 
        print('-' * 30)
        Student.view_all_student()


    elif choos == 2:                                           # For 2
        id = int(input('Enter the Student id: '))
        if Student.get_id(id):
            Student.enroll_student(id)
        else:
            print('Invalid Id')

    elif choos == 3:                                           # For 3
        id = int(input('Enter the Student id: '))
        if Student.get_id(id):
            Student.drop_student(id)
        else:
            print('Invalid Id')

    elif choos == 4:                                        # For 4
        break
    else:
        print('Invalid Number that you Chooss, Try Again.')


