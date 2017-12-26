import os
import sys
# 打印绝对路径
# E:\03学习\CasablancaPython_Pro\someExample\Test\test.py
print(os.path.abspath(__file__))
print(sys.argv[0])
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.abspath(sys.argv[0])))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# E:/03学习/CasablancaPython_Pro/someExample/Test/test.py
print(__file__)