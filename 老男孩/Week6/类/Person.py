
class Person:

    books=[]
    isok=''
    def __init__(self,name,age):
        """

        :param name:
        :param age:
        """
        self.name=name
        self.age=age

    def eat(self):
        print("我正在吃饭")

    def song(self):
        print("我正在唱歌")
    def say(self):
        bookNames= ','.join(self.books)
        print("大家好我是%s,今年%s岁了，我看过：%s"%(self.name,self.age,bookNames))

Person.books.append("python从入门到精通")
Person.isok='1'
p1=Person("流",30)
p1.books.append("卖火柴的小姑凉")
print("Person的isok为:%s"%Person.isok)
print("类变量赋值后为:%s"%p1.isok)
p1.isok='2'
print("Person的isok为:%s"%Person.isok)
print("p1为实例化Person，被类实例变脸替换了的类变量为%s"%p1.isok)
print("使用__class__的方式：%s"%p1.__class__.isok)
p2=Person("王",57)
p2.isok='3'
print("Person的isok为:%s"%Person.isok)
print("p1为实例化Person，被类实例变脸替换了的类变量为%s"%p1.isok)
print("p1为实例化Person，被类实例变脸替换了的类变量为%s"%p2.isok)

p2.books.append("十里桃花开")
p1.say()
p2.say()
