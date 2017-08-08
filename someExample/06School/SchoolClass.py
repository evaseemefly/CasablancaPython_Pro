from CourseClass import Course

class School:
    def __init__(self,name,address,city):
        self.name=name
        self.address=address
        self.city=city
        self.course=[]
        self.grade=[]

    def AddCourse(self,course):
        """
        添加课程
        :param course:课程对象
        :return:若添加进去则返回true，若已经存在则返回false
        """
        # 判断当前集合中是否包含当前课程
        if course in self.course:
            return False
        # 若不存在则将当前对象添加进去
        else:
            self.course.append(course)
            return True

    def AddGrade(self,grade):
        """
        添加课程
        :param grade:班级对象
        :return:若添加进去则返回true，若已经存在则返回false
        """
        # 判断当前集合中是否包含当前课程
        if g in self.grade:
            return False
        # 若不存在则将当前对象添加进去
        else:
            self.grade.append(grade)
            return True
