
L=['a1','b2','c3','d4','e5']

#取出前3个内容
#出现的错误
#TypeError: list indices must be integers or slices, not tuple 
#TypeError：列表索引必须是整数或片，不是元组
#切片中间是通过：切分，而非，
L[0:3]
print(L[0:4])
print(L[:4])
#找到倒数第3个
print(L[-1:])

#前4个数每两个取一个
print(L[0:4:2])