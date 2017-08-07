import pickle
import json

data={"name":"liu","age":30,"group":"group1"}
j_str=json.dumps(data)
print(j_str)
# 使用以下此种方式会报错
# print(json.dump(data))


decode_json=json.loads(j_str)
print(type(decode_json))
print(decode_json)
print(decode_json["name"])

# 读取json文件
with open('E:/03学习/CasablancaPython_Pro/老男孩/Week5/常用模块/test.json') as js:
    decode_test=json.load(js)
    print(decode_test)
    rows=decode_test["rows"]
    print(rows)
    print(type(rows))
    print(type(rows[0]))