import Player

class Human(Player.PlayerClass):
    """人类
    有get_move方法
    """
    def __repr__(self):
        return 'Human(%s)'%str(self)
    def get_move(self):
        while True:
            try:
                # 输入一个1-10的整数
                n=int(input('%s move (1-10):'%self.get_name))
                if 1<=n<=10:
                    return n
                else:
                    print('请按照规则输入!')
            except:
                print('请按照规则输入!')