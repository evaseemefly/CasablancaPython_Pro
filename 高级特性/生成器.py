#使用生成器实现斐波拉契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'

f=fib(6)

for n in f:
    print(n)

#生成器的练习
#杨辉三角定义如下：

#          1
#        1   1
#      1   2   1
#    1   3   3   1
#  1   4   6   4   1
#1   5   10  10  5   1
#把每一行看做一个list，试写一个generator，不断输出下一行的list：
#第n行的数字有n项。
#每行数字左右对称，由1开始逐渐变大。
#每个数等于它上方两数之和。
#步骤1：定义方法
def triangle(max):
    n=0
    while n<max:
        b=[]
        yield b
        b=[i for i in range(1,n)]
    pass