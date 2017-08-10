class Dog(object):
    # dogname="类属性——小鲁尔"
    def __init__(self,name):
        self.name=name

    # 类方法
    def eat(self):
        print("%s 正在吃饭"%self.name)
    # 类方法
    @property
    def eat(self):
        # 类方法只能调用类变量
        print("%s 正在吃饭 by静态方法" % self.name)

d=Dog("小九九")
# 调用属性方法需要像调用属性一样调用方法（调用时不加括号）
d.eat