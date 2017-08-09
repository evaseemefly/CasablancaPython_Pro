from CourseClass import Course
from GradeClass import Grade
from PersonClass import Person
from SchoolClass import School
from TeacherClass import Teacher
from StudentClass import Student


class TestClass:
    def __init__(self,name):
        self.name=name

# 1 创建学校
school1=School("北京it学院","北京市海淀区","beijing")
school2=School("上海it学院","上海浦东区","shanghai")
# print(school1)
# print(school2)

# 创建课程
course1=Course("linux","20周","1M")
course2=Course("go","22周","1.5M")
course3=Course("python","25周","1.2M")
# print(course1)
# print(course2)
# print(course3)
school1.AddCourse(course1)
school1.AddCourse(course2)
for c in school1.course:
    print(c)

# 创建老师及学生
student1=Student("casablanca",29,"M","1001","打篮球")

teacher=Teacher("drno",31,"M")
