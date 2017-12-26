import time
import  os,sys
sys.path.append(path.dirname(os.path.dirname(os.path.abspath(__file__))))
from day5 import package_test

print(time.process_time())
print(time.altzone)
print("---------")
print(time.asctime())
print(time.asctime((time.localtime())))
print(time.localtime())

print("--------Date----------")
# 将str类型的date转成struct格式
str2struct=time.strptime("2016/05/22","%Y/%m/%d")
print(str2struct)
struct2stamp=time.mktime(str2struct)
print(struct2stamp)

print("----gmtime-----")
print(time.gmtime(time.time()-86640))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()))
