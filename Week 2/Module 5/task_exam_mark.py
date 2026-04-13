class Exam:
    def __init__(self,mark,attand):
        self.attand = attand
        if not attand:
            self.mark = 0
        else:
            self.mark = mark
        self.min_mark = 5
        self.max_mark = 10
    
    def get_mark(self):
        if not self.attand:
            print(f'You are absent .Your marks is {self.mark}')
        else:
            print(f'Your marks is {self.mark}')

    def pass_or_fail(self):
        if self.mark < 5:
            print('Fail')
        elif self.mark > 10:
            print(' This mark has some problem.')
        else:
            print('Pass')

# Student No 01
print('Student No 01')
res = Exam(7,True)
res.get_mark() # Output : Your marks is 7
res.pass_or_fail() # Output : Pass

# Student No 02
print('Student No 02')
res2 = Exam(100,False)
res2.get_mark() # Output : You are absent .Your marks is 0
res2.pass_or_fail() # Output : Fail