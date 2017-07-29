#!_*_coding:utf-8_*_
import os
import sys
import logging

# print("/n")
# print(__file__)

# 获取当前项目所在路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DATA_BASE={
    'engine':'file_storage',
    'name':'accounts',
    'path':"%s/db"%BASE_DIR
}

LOG_LEVEL=logging.INFO

LOG_TYPES={
    'transaction':'transactions.log',
    'access':'access.log'
}

TRANSACTION_TYPE={
    'repay': {'action': 'plus', 'interest': 0},
    'withdraw': {'action': 'minus', 'interest': 0.05},
    'transfer': {'action': 'minus', 'interest': 0.05},
    'consume': {'action': 'minus', 'interest': 0},
}