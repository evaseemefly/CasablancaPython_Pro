import os
from core import db_handler
from conf import settings
from core import logger
import json
import time

def login_required(func):
    """验证用户是否登录
    """
    def wrapper(*args,**kwargs):
        if args[0].get('is_authenticated'):
            return func(*args,**kwargs)
        else:
            exit("用户未授权")
    return wrapper

def acc_auth(account,pwd):
    """"
    根据账户名称与密码进行验证
    """
    db_api=db_handler.db_handler()
    data=db_api("select * from accounts where account=%s"%account)
    if data['pwd']==pwd:
        # time.strptime 根据指定的格式把一个时间字符串解析为时间元组
        # time.mktime(t)
        # 将一个t（时间元组）转换为s表示的浮点数
        exp_time_stamp=time.mktime(time.strptime(data['expire_date'],"%Y-%m-%d"))
        # time.time 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
        # 若当前的时间戳大于过期时间的时间戳，则说明登录已经超过期限
        if time.time()>exp_time_stamp:
            print("卡片以过期")
        else :
            return data
    else:
        print("指定账户不存在")

    # account_file="%s/%s.json"%(db_path,account)
    # print(account_file)
    # if os.path.isfile(account_file):
    #     with open(account_file,'r') as f:
    #         account_data=json.load(f)
    #         if account_data['pwd']==pwd:
    #             # time.strptime 根据指定的格式把一个时间字符串解析为时间元组
    #             # time.mktime(t)
    #             # 将一个t（时间元组）转换为s表示的浮点数
    #             exp_time_stamp=time.mktime(time.strptime(account_data['expire_date'],"%Y-%m-%d"))
    #             # time.time 返回当前时间的时间戳（1970纪元后经过的浮点秒数）
    #             # 若当前的时间戳大于过期时间的时间戳，则说明登录已经超过期限
    #             if time.time()>exp_time_stamp:
    #                 print("卡片以过期")
    #             else :
    #                 return account_data
    #         else:
    #             print("指定账户不存在")

def acc_login(user_data,log_obj):
    '''
    account login func
    :user_data: user info data , only saves in memory
    :return:
    '''
    retry_count = 0
    while user_data['is_authenticated'] is not True and retry_count < 3 :
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth = acc_auth(account, password)
        if auth: #not None means passed the authentication
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            #print("welcome")
            return auth
        retry_count +=1
    else:
        log_obj.error("account [%s] too many login attempts" % account)
        exit()