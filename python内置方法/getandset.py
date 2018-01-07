
class Animal:
    classname='Animal'
    def __init__(self,name):

        self.name=name

    def eat(self):
        print("%s在吃饭"%self.name)

animal=Animal("小鸡")

print(getattr(animal,'classname'))
print(getattr(animal,'name'))
method=getattr(animal,'eat')
method()

