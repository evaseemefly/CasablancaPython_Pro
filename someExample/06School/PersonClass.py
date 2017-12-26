
def say():
    print("测试")

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        
class Test(Person):
    def __init__(self):
        super(Test, self).__init__()