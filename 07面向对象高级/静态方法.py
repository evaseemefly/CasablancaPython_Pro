
class Dog(object):
    def __init__(self,name):
        self.name=name

    # 类方法
    def eat(self):
        print("%s 正在吃饭"%self.name)
    # 静态方法
    @staticmethod
    def eat(self):
        print("%s 正在吃饭 by静态方法"%self.name)
d=Dog("小九九")
d.eat(d)
