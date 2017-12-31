
class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print("我正在吃饭，我是%s"%self.name)

    def howoldru(self):
        # 父类无法访问子类的私有方法或属性
        print(self.__age)
        # print(self.age)

    def __sweep(self):
        print("我正在梳理毛发")

    

class Cat(Animal):
    def __init__(self,name):
        # 注意使用super 调用父类的构造函数时，第一个参数是子类！切记
        super(Cat, self).__init__(name)

    def fathereat(self):
        print("准备调用父类的吃饭方法")
        self.eat()
    
    @property
    def __age(self):
        return 

    def fathersweep(self):
        '''
        子类无法调用父类的私有方法
        :return:
        '''
        self.__sweep()

def main():
    cat=Cat('kimi')
    cat.fathereat()
    # cat.fathersweep()
    cat.howoldru()


if __name__ == '__main__':
    main()
    
