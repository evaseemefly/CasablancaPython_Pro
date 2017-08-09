from CourseClass import Course
from TeacherClass import Teacher
import time

class Grade(object):
    def __init__(self,name):
        """
        通过学校创建班级， 班级关联课程、讲师
        :param name:班级名称
        """
        self.name=name
        self.date = time.time() #开课时间
        self.course=[] #课程集合
        self.students=[] #学生集合
        self.teacher

    def addCourse(self,course):
        """
        为当前班级添加课程
        :param course:课程
        :return:
        """
        if course in self.course:
            return False
        else:
            self.course.append(course)
            return True

    def addTeacher(self,teacher):
        """
        为当前班级添加老师
        :param teacher:
        :return:
        """
        if self.teacher==teacher:
            return False
        else:
            self.teacher=teacher

    def GetStudentList(self):
        '''
        返回当前班级中的学生列表
        :param self:
        :return:
        '''
        return self.students
