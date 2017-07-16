import Player
import Human
import Undercut
import Computer
import Undercut

p=Player.PlayerClass('搜索')
print("Player:%s"%p)
print("Human:%s"%Human.Human('测试'))
# def main():
#     print('测试')
#     p=Player('刘')
#     print(p)

# 下面进行玩Undercut的demo
c1=Computer.Computer('疯狂的电脑1')
c2=Computer.Computer('疯狂的电脑2')
# h=Human.Human('liu')
result=Undercut.play_undercut(c1,c2)
print(result)
