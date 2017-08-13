class Dog(object):
    dogname="类属性——小鲁尔"
    def __init__(self,name):
        self.name=name

    # 类方法
    def eat(self):
        print("%s 正在吃饭"%self.name)
    # 类方法
    @classmethod
    def eat(self):
        # 类方法只能调用类变量
        print("%s 正在吃饭 by静态方法" % self.dogname)

d=Dog("斯蒂芬斯蒂芬")
d.eat()