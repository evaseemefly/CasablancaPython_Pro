#!_*_coding:utf-8_*_
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import settings

def file_db_handle(conn_params):
    """
    :param conn_params:db连接参数
    :return:
    """
    print(('file db:%s'%conn_params))

    return  file_execute

def db_handler():
    conn_params=settings.DATA_BASE
    if conn_params['engine']=='file_storage':
        return  file_db_handle(conn_params)
    elif conn_params['engine']=='mysql':
        pass

def file_execute(sql,**kwargs):
    conn_params=settings.DATA_BASE
    # 从配置文件中读取path和name
    db_path="%s/%s"%(conn_params['path'],conn_params['name'])
    print(sql,db_path)

    sql_list=sql.split("where")
    print(sql_list)
    # 如果sql_list集合是一个select语句
    if sql_list[0].startswith("select") and len(sql_list)>1:
        # 删除sql_list[1]头尾的空格（strip默认为空格）并以=分隔
        column,val=sql_list [1].strip().split("=")
        if column=='account':

            account_file="%s%s.json"%(db_path,val)
            print(account_file)
            if os.path.isfile((account_file)):
                with open(account_file,'r') as f:
                    account_data=json.load(f)
                    return account_data
            else:
                exit("Account[%s]不存在"%val)
    elif sql_list[0].startswith("update") and len(sql_list)>1:
        column,val=sql_list [1].strip().split("=")
        if column == 'account':
            account_file = "%s%s.json" % (db_path, val)
            print(account_file)
            if os.path.isfile((account_file)):
                account_data=kwargs.get("accoun_data")
                with open(account_file,'w') as f:
                    acc_data=json.dump(account_data,f)
                    return True




db_handler()
file_execute("select * from db")
# from  conf import settings
