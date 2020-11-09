# coding=utf-8

# A QQBot using CQHTTP with coolQ and nonebot api

# Coded by Kurikai_Sakuri

# Environment: Python 3.7.6 64-bit on Windows 10

# Including Libraries:

'''
    aiocqhttp
    cn2an
    datetime
    hashlib
    jieba
    nonebot
    os
    pytz
    random
    requests
    selenium
    tweepy
    urllib
'''

# Other supporting softwares:

'''
    酷Q
    ----CQHttp plugin
'''

# How to install:
#   check:
#       https://cqhttp.cc/
#       https://cqp.cc/

# Notice: To make CQHttp send message to nonebot,
#   you should change the configuration in:
#   (installation path of coolQ)/data/app/io.github.richardchien.coolqhttpapi/config/<user-id>.json
#   check: https://nonebot.cqp.moe/guide/getting-started.html

from os import path

# nonebot api
import nonebot

# configuration of nonebot in './config.py'
import config

if __name__ == '__main__':
    # parameter:
    #   None
    # return:
    #   None

    # initialization for nonebot
    nonebot.init(config)

    # load plugins for nonebot
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'shokobot', 'plugins'),
        'shokobot.plugins'
    )

    # run nonebot
    nonebot.run()
