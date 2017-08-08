class School(object):
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.students = []
        self.staffs = []

    def enroll(self, stu):
        print("为学员%s办理注册手续" % stu.name)
        self.students.append(stu)

    def hire(self, staff_obj):
        print("雇佣新的老师%s"%staff_obj.name)
        self.staffs.append(staff_obj)

class SchoolMember(object):
    def __init__(self, name, age, sex):
        self.name=name
        self.age=age
        self.sex=sex
    
    def tell(self):
        pass

class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        #实现继承父类可使用super的方式
        super(Teacher, self).__init__(name,age,sex)
        self.salary=salary
        self.course=course

    def tell(self):
        print('''
        ————info of teacher:%s————
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print("%s is teaching course [%s]" %(self.name,self.course))


class Student(SchoolMember):
    def __init__(self, name, age, sex,stu_id,grade):
        super(Student,self).__init__(name, age, sex)
        self.stu_id=stu_id
        self.grade=grade
    def tell(self):
        print('''
        ————Info of Student:%s——————
        Name:%s
        Age:%s
        Sex:%s
        Stu_id:%s
        Grade:%s

        '''%(self.name,self.name,self.age,self.sex,self.stu_id,self.grade))

    def pay_tution(self,amount):
        print("%s has paid tution for %s"%(self.name,amount))

school=School("北京42中","西城区")

t1=Teacher("张春梅",30,"F",2000,"语文")
t2=Teacher("邓连庆",32,"M",5000,"物理")

s1=Student("刘","29","M",1001,"语文")

t1.tell()
s1.tell()

school.hire(t1)
school.enroll(s1)

school.staffs[0].teach()

for stu in school.students:
    stu.pay_tution(5000)
    