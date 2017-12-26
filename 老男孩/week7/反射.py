

class Person(object):
    count=0
    def __init__(self,name,count):
        self.name=name
        self.count=count

    def say(self,yourname):
        print("hi %s,I'm %s"%(yourname,self.name))

# 若在类的外部定义方法，通过反射供指定实例对象使用时
# 需要注意为外部方法加入self参数
def bye(self):
    print("再见啦")

p=Person("casablanca",10)
str_input=input("请输入方法的名称：").strip()

if hasattr(p,str_input):
    # 注意使用getattr获取实例对象中的指定字符串名称的属性或方法时
    # 1 调用方法并传入指定参数，需要有一个变量接收通过getattr获取到的方法，调用时需要加上（）
    # 2 若反射的为属性，则不需要加括号
    func= getattr(p,str_input)
    print(func)
    func("dr.no")
else:
    setattr(p,str_input,bye)
    func=getattr(p,str_input)
    func(p)


