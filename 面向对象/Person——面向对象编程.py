class Person:
    """人
    """
    # 构造函数
    def __init__(self):
        self.name=''
        # 两个下划线代表该变量是私有变量
        self.__age=0
    def __init__(self,name='',age=0):
        self.name=name
        self.__age=age
    def set_age(self,age):
        if 0<age<=150:
            self.__age=age
    def display(self):
        print("Person('%s',age%d)"%(self.name,self.__age))
    # 用于生成对象的字符串表示
    def __str__(self):
        return "Person('%s',%d)"%(self.name,self.__age)
    # 返回对象的官方表示，可自定义
    def __repr__(self):
        return str(self)

p=Person('casablanca',29)
#print(p)
print(p)
# p.display()
print(str(p))
print('修改年龄')
p.set_age(30)
# p.age(40)
p.__age(50)
print(p)
p.set_age(200)
print(p)
