'''
    字段代码为 python cookbook 10.10 使用延迟计算属性
    by evaseemelfly
'''


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        '''
            面积
        :return:
        '''
        print('计算圆')
        return math.pi * self.radius ** 2

    def perimeter(self):
        '''
            周长
        :return:
        '''
        print('计算周长')
        return 2 * math.pi * self.radius


c = Circle(4.0)
c.radius

c.area

'''
    10.9 8.9 通过描述其类的形式来定义一个全新的实例属性
'''


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        print('进入了__get__')
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value,int):
            raise TypeError('不是int类型')
        instance.__dict__[self.name]=value


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p=Point(2,3)
p.x=5
# p.y=2.5


class Person:

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print("Getting: %s" % self._name)
        return self._name

    @name.setter
    def name(self, value):
        print("Setting: %s" % value)
        self._name = value.title()

    @name.deleter
    def name(self):
        print(">Deleting: %s" % self._name)
        del self._name

person=Person()
person.name="小王"
print(person.name)