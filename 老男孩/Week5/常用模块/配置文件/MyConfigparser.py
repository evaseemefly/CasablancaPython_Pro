import configparser

conf=configparser.ConfigParser()
# 一、读取配置文件
# 读取指定路径的配置文件
conf.read('MyConf.ini')
# 读取配置节
print(conf.sections())
# 可以看到所有的配置节是一个list
print(type(conf.sections()))
# 判断指定名称的配置节是否在配置文件中
temp='bitbucket.org' in conf
print(temp)
# 读取配置文件
print(conf["bitbucket.org"]['User'])
temp_server=conf["topsecret.server.com"]
# <class 'configparser.SectionProxy'>
print(type(temp_server))
print(temp_server["Port"])
# user=conf["bitbucket.org"]['User']
# print(user)

# 二、写入配置文件
# 配置节/添加的项/value
# conf.set('topsecret.server.com','Ip','192.168.1.1')
# conf.write(open('MyConf.ini','w'))

# 三、删除配置节
conf.remove_option('topsecret.server.com','Ip')
conf.write(open('MyConf.ini','w'))