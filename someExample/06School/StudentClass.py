from PersonClass import Person
# import Person
import sys

# print(sys.path)
print(Person)
p1=Person("liu",29,"F")
# say()
# Person.say()
# Person.say()

# p1=Person("liu",29,"M")

class Student(Person):
    def __init__(self,name,age,gender,id,hobby):
        super(Student, self).__init__(name,age,gender)
        self.id=id
        self.hobby=hobby
    # def __init__(self,name,age,gender,hobby):
    #     self.name
    #     self.age
    #     self.gender
    #     self.hobby=[]

    def Register(self):
        '''
        对学员进行注册
        注册成功后学员应加入指定的班级之中
        :return:
        '''
        print('''
        ————详细信息————
        学员id:%s
        姓名：%s
        年龄：%s
        现在进行注册
        '''%(self.id,self.name,self.age))

    def Pay(self,payment):
        print('''
               ————详细信息————
               学员id:%s
               姓名：%s
               年龄：%s
               现在进行缴费：%s
               ''' % (self.id, self.name, self.age,payment))

    def GetGradeList(self):
        '''
        获取班级列表
        :return:
        '''
        pass

    def ChoiceTargetGrade(self,id):
        '''
        根据id选择班级
        :param id:
        :return:
        '''
        pass
