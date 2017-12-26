import logging
# from conf import settings
# import conf.settings
# from conf import settings
# from bin import atm
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
import logging
from conf import settings

def logger(log_type):
    """
    以名称创建的logger对象
    :param log_type:创建的logger对象的名称
    :return:logger
    """
    # 1-1 根据指定类型（str）创建logger
    logger=logging.getLogger(log_type)
    # 1-2 设置日志等级
    logger.setLevel(settings.LOG_LEVEL)
    # 2-1 创建Handler
    # StreamHandler默认是sys.stderr.
    ch=logging.StreamHandler()
    # 2-2 设置记录日志的等级
    ch.setLevel(settings.LOG_LEVEL)
    # 2-3 输出的日志路径
    # log_file="%s/log/%s"%(settings.BASE_DIR,settings.LOG_LEVEL[log_type])
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_TYPES[log_type])
    fh=logging.FileHandler(log_file)
    # 2-4 输出的日志内容格式
    formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 2-5 将添加handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    return  logger



