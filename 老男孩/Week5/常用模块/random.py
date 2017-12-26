import time
import os,sys
import random

# 只会输出0-1的随机数
print(random.random())
# 输出从a-b的int类型随机数
print(random.randint(1, 10))

print(random.choice('liusihan'))

# 生成随机验证码
checkcode=''
for i in range(4):
    current=random.randrange(0,4)
    if current!=i:
        temp=chr(random.randint(65,90))
    else:
        temp=random.randint(0,9)
    checkcode+=str(temp)
print(checkcode)