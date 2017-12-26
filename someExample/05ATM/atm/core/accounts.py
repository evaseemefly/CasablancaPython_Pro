#用于从文件里加载和存储账户数据
import json
import time
from core import db_handler
from conf import settings

def load_current_balance(account_id):
    """
    根据穿入的账户id返回该账户的基本信息
    :param account_id:
    :return:
    """
    db_api=db_handler.db_handler()
    data=db_api("select * from accounts where account=%s"%account_id)

    return data

def dump_account(account_data):
    db_api=db_handler.db_handler()
    data=db_api("update accounts where account=%s"%account_data['id'],account_data=account_data)
    return True