# TwitterToQQBot

A QQbot to push Tweets to QQ group

一个QQBot，基于酷Q的CQHTTP插件和[nonebot API](https://github.com/nonebot/nonebot)编写

开发环境：Python 3.7.6 64-bit on Windows 10

## 简介

自动推送并翻译（使用百度翻译API）复数指定账号的推文

手动按时间顺序查询并翻译复数推文

进行简单的互动

定时发布信息

掷色子


目前应用于[多间硝子](https://space.bilibili.com/20621838)字幕组组内的推特推送Bot。

## 使用之前

请先准备：

一个作为Bot的QQ号

百度翻译的API

twitter的API

一个ssr代理

## 环境安装

### Python 环境

推荐使用python 3.7

需要安装如下库：

```
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
```
### 其他环境

#### ~~酷Q Pro~~

--由于酷Q被封，现在转而使用[mirai](https://github.com/mamoe/mirai-console)框架，使用[CQHTTPmirai](https://github.com/yyuueexxiinngg/cqhttp-mirai)插件进行移植--

如何安装mirai和CQHTTPmirai请移步。

#### CQHTTP插件配置

安装好mirai和CPHTTPmirai插件后，打开插件文件夹下的setting.yml，做如下修改：

```
# Debug日志输出选项
debug: false
# 要进行配置的QQ号 (Mirai支持多帐号登录, 故需要对每个帐号进行单独设置)
'123456789': # 这里改成你想要作为bot的QQ号
  # HTTP 相关配置
  http:
    # 可选，是否启用HTTP API服务器, 默认为不启用, 此项开始与否跟postUrl无关
    enable: false
    # 可选，HTTP API服务器监听地址, 默认为0.0.0.0
    host: 0.0.0.0
    # 可选，HTTP API服务器监听端口, 5700
    port: 5700
    # 可选，访问口令, 默认为空, 即不设置Token
    accessToken: ""
    # 可选，事件及数据上报URL, 默认为空, 即不上报
    postUrl: ""
    # 可选，上报消息格式，string 为字符串格式，array 为数组格式, 默认为string
    postMessageFormat: string
    # 可选，上报数据签名密钥, 默认为空
    secret: ""
  # 可选，反向客户端服务
  ws_reverse:
    # 可选，是否启用反向客户端，默认不启用
    - enable: true
      # 上报消息格式，string 为字符串格式，array 为数组格式
      postMessageFormat: string
      # 反向Websocket主机
      reverseHost: 127.0.0.1
      # 反向Websocket端口
      reversePort: 8081
      # 访问口令, 默认为空, 即不设置Token
      accessToken: ""
      # 反向Websocket路径
      reversePath: /ws
      # 可选, 反向Websocket Api路径, 默认为reversePath
      reverseApiPath: /api
      # 可选, 反向Websocket Event路径, 默认为reversePath
      reverseEventPath: /event
      # 是否使用Universal客户端 默认为true
      useUniversal: true
      # 反向 WebSocket 客户端断线重连间隔，单位毫秒
      reconnectInterval: 3000
    - enable: true # 这里是第二个连接, 相当于CQHTTP分身版
      postMessageFormat: string
      reverseHost: 127.0.0.1
      reversePort: 8081
      reversePath: /ws
      useUniversal: false
      reconnectInterval: 3000
  # 可选，正向Websocket服务器
  ws:
    # 可选，是否启用正向Websocket服务器，默认不启用
    enable: false
    # 可选，上报消息格式，string 为字符串格式，array 为数组格式, 默认为string
    postMessageFormat: string
    # 可选，访问口令, 默认为空, 即不设置Token
    accessToken: ""
    # 监听主机
    wsHost: "0.0.0.0"
    # 监听端口
    wsPort: 8080
```

## 如何配置

下载源码后请在config.py中修改：

```
# The superusers for nonebot
# Only superusers can use some command such as /say
SUPERUSERS = {
    123456789, # 不是作为Bot的QQ号！
    1145141919 # 不是作为Bot的QQ号！
}

...

# Reserving IP
# 这里与上一步配置的ip一致
HOST = '127.0.0.1'
PORT = 8081

# To communicate with CQHttp API
# 这里与上一步配置的ip一致
API_ROOT = 'http://127.0.0.1:8081'
```

然后打开/shokobot/settings.py,做如下改动
```
# Configurations for plugins
from os import path

twitter_id = {
    'Tamashoko_',
    'Tama_Glass' # 想要自动推送的推特账号
}
user_ids = {
    123432123 # 自动推送的QQ账号对象
}

group_ids = {
    1919810,  # 自动推送的QQ群组对象
    11451419
}

last_id_cachepath = path.join(path.dirname(__file__), 'cache', 'lastid.txt')
# image_cachepath = path.join(path.dirname(__file__), 'cache', 'imgcache')
image_cachepath = r'C:\Users\DJDJD\Desktop\CQP-tuling\酷Q Pro\data\image' # 可以自定义图片缓存的路径

translate_api_url_http = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

# 填入百度翻译API的如下信息
translate_app_id = '' 
translate_password = ''

# 填入twitterAPI的如下信息
twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_token_secret = ''

# 填入代理信息
ssr_proxy_http = "http://127.0.0.1:1081"
ssr_proxies = {
    "http":"http://127.0.0.1:1081",
}
```

至此即配置完毕。
运行miraiOK_windows_386.exe，运行main.py，若在控制台中输出
```
[2020-11-09 15:32:08,511 nonebot] INFO: Succeeded to import "shokobot.plugins.auto_push"
[2020-11-09 15:32:09,060 nonebot] INFO: Succeeded to import "shokobot.plugins.conversation"
[2020-11-09 15:32:09,062 nonebot] INFO: Succeeded to import "shokobot.plugins.dicegame"
[2020-11-09 15:32:09,164 nonebot] INFO: Succeeded to import "shokobot.plugins.manual_push"
[2020-11-09 15:32:09,171 nonebot] INFO: Succeeded to import "shokobot.plugins.schedule_notice"
[2020-11-09 15:32:09,295 nonebot] INFO: Succeeded to import "shokobot.plugins.screenshots"
[2020-11-09 15:32:09,296 nonebot] INFO: Succeeded to import "shokobot.plugins.settings"       
[2020-11-09 15:32:09,298 nonebot] INFO: Succeeded to import "shokobot.plugins.translate"      
[2020-11-09 15:32:09,300 nonebot] INFO: Succeeded to import "shokobot.plugins.translate_tweet"
[2020-11-09 15:32:09,302 nonebot] INFO: Succeeded to import "shokobot.plugins.twitter"        
[2020-11-09 15:32:09,303 nonebot] INFO: Succeeded to import "shokobot.plugins.usage"
[2020-11-09 15:32:09,304 nonebot] INFO: Running on 127.0.0.1:8081
Running on http://127.0.0.1:8081 (CTRL + C to quit)      
[2020-11-09 15:32:09,311 nonebot] INFO: Scheduler started
[2020-11-09 15:32:09,313] Running on 127.0.0.1:8081 over http (CTRL + C to quit)
[2020-11-09 15:32:10,808] 127.0.0.1:9649 GET /ws 1.1 101 - 10616
[2020-11-09 15:32:10,820] 127.0.0.1:9647 GET /ws 1.1 101 - 21591
```
表明已经成功启动，可以与机器人聊天互动了

## 常用指令

Bot可以做到一定程度的自然语言处理，以下指令都可以适用：


bot，推送最近五条推文

机器人 翻译最近三条推特

烤推机。推送第1条推文

@机器人，我好看吗


投色子的语法如下：

bot，dice 1d6


未识别为指令的唤起将被作为对话处理，机器人会进行一个简单的回答。

## 自定义

查阅config.py中的注释，进行机器人基础设定的其他自定义

参考[nonebot文档](https://docs.nonebot.dev/)，对shokobot/下的插件进行深度修改

## 参考

https://github.com/mamoe/mirai-console
https://github.com/nonebot/nonebot
https://docs.nonebot.dev/
https://github.com/yyuueexxiinngg/cqhttp-mirai

## 其他

感谢框架开发者们一直以来的辛勤付出

本人技术不足，放出代码仅供参考，意见建议欢迎PR
