import datetime
import time

class Course:
    def __init__(self,name,period,price):
        """
            课程包含，周期，价格，通过学校创建课程 
        :param name:课程名称
        :param period:课程周期
        :param price:课程价格
        """
        self.name=name
        self.period=period
        self.price=price
        self.teachers=[]

    def __str__(self):
        return ('''
                ——CourseInfo——
                Name:%s
                Period:%s
                Price:%s
                
                ''' % (self.name, self.period, self.price))