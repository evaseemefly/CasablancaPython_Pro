# __by__:'casablanca'

import json
account_dic={
    'id':1,
    'name':'admin',
    'pwd':'abc',
    'credit':15000,#信用账户
    'balance':15000,#余额
    'subtime':'2017-07-01',
    'duetime':'2021-01-01',
    'status':0 #0=正常，1=锁定，2=取消
}

print(json.dumps(account_dic))