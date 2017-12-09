class Student:
    age=18
    def __init__(self):
        self.name="myname"
        pass
    def testfunc(self):
        print('testfunc')
        pass
class Test:
    def __init__(self):
        pass

    def extfunc(self):
        print('extfunc')

class Adapter:
    def __init__(self,obj,method):
        self.obj=obj
        self.__dict__.update(method)

def main():
    stu=Student()
    test=Test()
    # 若查看某个具体的对象（实例化后）的dict返回的是该对象自己的属性
    # print(test.__dict__)
    # print(stu.dic())
    # Student.__dict__.update(extfunc=Test.extfunc)
    Adapter(test,dict(testfunc=Test.extfunc))
    # stu.extfunc()
    # 若查看指定class的dict则是该class中的类变量，以及方法
    print(test.__dict__)
    test.testfunc()
    st=Student()
    # st.extfunc()
    pass

if __name__=='__main__':
    main()



