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

# d=Dog("小九九")
# 调用属性方法需要像调用属性一样调用方法（调用时不加括号）
# d.eat

# 关于属性方法的另一个示例
class Flight(object):
    '''
    航班类
    '''
    def __init__(self,name):
        self.flight_name=name
        self.__flight_checked=False

    def checking_status(self):
        print("检查航班%s 状态"%self.flight_name)
        return 1

    @property
    def flight_status(self):
        status=self.checking_status()
        if status==0:
            print("航班已取消")
        elif status==1:
            print("航班已到达")
        elif status==2:
            print("无法确认航班状态，请稍后再查")

    @flight_status.setter
    def flight_status(self,status):
        status_dic={
            0:"取消",
            1:"到达",
            2:"延误"
        }
        print("航班状态已被更改为%s"%status_dic.get(status))

    @property
    def flight_checked(self):
        return  self.__flight_checked

    @flight_checked.setter
    def flight_checked(self,checked):
        self.__flight_checked=checked
        return  self.__flight_checked

f=Flight("CA980")
f.flight_status
f.flight_status=1
print(f.flight_checked)
f.flight_checked=True
print(f.flight_checked)

print(Flight.__doc__)
print(f.__module__)
print(f.__class__)