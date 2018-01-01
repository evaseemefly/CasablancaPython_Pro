from enum import Enum

TreeType=Enum('TypeType','apple_tree,cherry_tree')


class Tree:
    '''
    池是一个字典
    '''
    pool=dict()

    def __new__(cls, *args, **kwargs):
        '''


        :param args:
        :param kwargs:
        :return:
        '''

        '''
        *args 表示任何多个无名参数，它是一个tuple；
        **kwargs 表示关键字参数，它是一个dict。
        并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前
        '''

        # 判断
        obj=cls.pool.get(kwargs['tree_type'],None)
        if not obj:
            obj=object.__new__(cls)
            cls.pool[kwargs['tree_type']]=obj
            obj.tree_type=kwargs['tree_type']
        return obj

t1=Tree(tree_type=TreeType.apple_tree)
t2=Tree(tree_type=TreeType.apple_tree)
print(id(t1))
print(id(t2))


def main():
    pass


if __name__ == '__main__':
    main()

