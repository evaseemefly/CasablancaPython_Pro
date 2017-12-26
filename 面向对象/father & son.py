class A(object):
    # def __init__(self):
    #     self.name="123"
    def __init__(self,name):
        self.name=name

    def sayhi(self):
        print(self.name)
        
class B(A):
    Age=0
    def __init__(self,name,age):
        super(B, self).__init__(name)
        Age=age

    def sayhiB(self):
        print(self.name)

    class D:
        def __init__(self,name):
            self.name=name
    class C(A):
        def __init__(self,name):
            # 当实例化B后，调取B的示例对象b时，类变量Age还是0
            self.age=B.Age
            super(B.C, self).__init__(name)
b=B("测试",18)
# c=B.C("CAO")
c=b.C("CAO")
print(c.age)
c.sayhi()
c.sayhiB()