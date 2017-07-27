import time
def consumer(name):
    print("%s准备吃饭了" % name)
    while True:
        food=yield
        print("%s吃了%s"  % (name,food))
def producer(name):
    c1=consumer('zhangsan')
    c2=consumer('lisi')
    c1.__next__()
    c2.__next__()
    print("准备吃饭")
    for i in range(10):
        time.sleep(1)
        print("做了一份饭")
        c1.send(i)
        c2.send(i)

producer("alex")