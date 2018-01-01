
class MyDict:
    country='China'

    def __init__(self,name):
        self.name=name
        pass

    def add(self,num):
        pass


mydict=MyDict("whomI")
print("实例化后的对象的__dict__方法%s"%mydict.__dict__)

print("类的__dict__方法%s"%MyDict.__dict__)