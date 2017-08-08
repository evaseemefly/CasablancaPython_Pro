from PersonClass import Person

class Teacher(Person):
    def __init__(self,name,age,gender):
        super(Teacher, self).__init__(name,age,gender)
        self.grades=[]

    def GetGradeList(self):
        pass

    def GetStudentList(self):
        pass

    def AddGrades