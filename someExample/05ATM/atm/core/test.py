# from conf import settings
import os
import sys
from core import main
# BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# from bin import atm
from core import logger
from conf import settings
# type_obj=settings.LOG_TYPES
log=logger.logger("transaction")
log.info("测试日志内容")