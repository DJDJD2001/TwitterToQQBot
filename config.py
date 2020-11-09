# This is the configuration for nonebot

from nonebot.default_config import *

# Debug mode
DEBUG = False

# The superusers for nonebot
# Only superusers can use some command such as /say
SUPERUSERS = {
    123456789, # your own QQ
    1145141919 # your another QQ
}

# Prefix to call command
COMMAND_START = {
    '',
    '/',
    '!',
    '／',
    '！'
}

# Seperator in command
COMMAND_SEP = {
    '/',
    '.'
}

# To wake the bot
NICKNAME = {
    'bot',
    'shokobot',
    '机器人',
    '烤推机'
}

# Reserving IP
# Same as IP in CQHttp
# If running in another os, you should change them
#   check: https://nonebot.cqp.moe/guide/getting-started.html
HOST = '127.0.0.1'
PORT = 8081

# To communicate with CQHttp API
# Same as IP in CQHttp
# If running in another os, you should change them
#   check: https://nonebot.cqp.moe/guide/getting-started.html
API_ROOT = 'http://127.0.0.1:8081'

# Timeout settings
from datetime import timedelta
SESSION_EXPIRE_TIMEOUT = timedelta(minutes = 2)
SESSION_RUN_TIMEOUT = timedelta(seconds = 10)

# Tips
SESSION_RUNNING_EXPRESSION = '(＾ｰ^)您有命令正在执行，请稍后再试……！'
DEFAULT_VALIDATION_FAILURE_EXPRESSION = '(＾ｰ^)您发送的内容格式不太对呢……！'
TOO_MANY_VALIDATION_FAILURES_EXPRESSION = '(＾ｰ^)您输错太多次啦，请重新尝试……！'
SESSION_CANCEL_EXPRESSION = '(＾ｰ^)好的……！'

# Max length of input message
SHORT_MESSAGE_MAX_LENGTH = 100

# Max tries of input failures
MAX_VALIDATION_FAILURES = 3
