__by__='casablanca'

product_list=[
    ('Iphone' , 4900),
    ('Mac Pro' , 9800),
    ('Bike',800),
    ('Watch',10600)
    ]

shopping_list=[]
salary=input("请输入你的薪水")
print('你的薪水为%s'%salary)
# 判断输入的薪水是否只有数组组成
if salary.isdigit():
    salary=int(salary)
    while True:
        # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice=input('要买什么？')
        if user_choice.isdigit():
            user_choice=int(user_choice)
            # 判断用户选择id是否在已经序列内，且是否有效
            if user_choice<len(product_list) and user_choice>=0:
                # 根据下标取出对应的对象
                p_item=product_list[user_choice]
                # 注意取出的对象是一个数组
                # 第2个，即下标为1的为value
                if p_item[1]<=salary:
                    # 将序号及value加入list中
                    shopping_list.append(p_item)
                    # 余额减去当前的金额
                    salary-=p_item[1]
                    print("已将%s放入你的购物车，你的当前余额为%s"%(p_item,salary))
                else:
                    print("没钱了")
            else:
                print("输入有误")
        elif  user_choice=='q':
            print("————————购物车——————————")
            for p in shopping_list:
                print(p)
            print("你的当前剩余余额为：%s"%salary)
            exit()
    else:
        print("未知错误")        
