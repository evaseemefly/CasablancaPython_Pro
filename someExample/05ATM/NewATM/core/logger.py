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

    logger=logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)
