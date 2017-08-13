
class Foo(object):
    def __init__(self):
        self.dic={}
    def __getitem__(self, item):
        print("getitem")
        return self.dic.get(item)
    def __setitem__(self, key, value):
        print("setitem :%s :%s"%(key,value))
        self.dic[key]=value

obj=Foo()
obj["name"]="casablanca"
print(obj["name"])

