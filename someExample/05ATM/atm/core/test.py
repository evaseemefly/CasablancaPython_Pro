# from conf import settings
import os
import sys
# from core import main
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# from bin import atm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core import accounts

# 测试读取账户信息功能
acc=accounts.load_current_balance('1234')
print(acc)
# type_obj=settings.LOG_TYPES
# 测试日志功能
# log=logger.logger("transaction")
# log.info("测试日志内容")

