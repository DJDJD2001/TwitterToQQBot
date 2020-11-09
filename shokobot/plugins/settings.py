# Configurations for plugins
from os import path

twitter_id = {
    'Tamashoko_',
    'Tama_Glass'
}
user_ids = {
    1145141919810
}

group_ids = {
    7892347890
}

last_id_cachepath = path.join(path.dirname(__file__), 'cache', 'lastid.txt')
# image_cachepath = path.join(path.dirname(__file__), 'cache', 'imgcache')
image_cachepath = r'C:\Users\DJDJD\Desktop\CQP-tuling\酷Q Pro\data\image'

translate_api_url_http = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
translate_app_id = ''
translate_password = ''

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_token_secret = ''

ssr_proxy_http = "http://127.0.0.1:1081"
ssr_proxies = {
    "http":"http://127.0.0.1:1081",
}
