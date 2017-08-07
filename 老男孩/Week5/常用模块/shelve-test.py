import shelve
import datetime

d = shelve.open('shelve_mytest')  # 打开一个文件

class Person(object):
    def __init__(self,age):
        self.age=age

person1=Person(9)
person2=Person(10)

name=["liu","wang"]
d["test"]=name
d["p1"]=person1
d["p2"]=person2

print(d.get("test"))
print(d.get("p1"))
print(d.get("p2"))
