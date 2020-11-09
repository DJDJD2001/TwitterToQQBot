import nonebot
import os
import requests
import tweepy
import re

from shokobot.plugins.settings import last_id_cachepath
from shokobot.plugins.settings import image_cachepath
from shokobot.plugins.settings import group_ids
from shokobot.plugins.settings import ssr_proxies
from shokobot.plugins.settings import twitter_id as IDs

from shokobot.plugins.twitter import twitter_get_api
from shokobot.plugins.translate import translate

# For debug
from shokobot.plugins.settings import user_ids

__plugin_name__ = '推送最新推文'
__plugin_usage__ = r'''
自动检测并推送最新推文
'''

@nonebot.scheduler.scheduled_job('interval', seconds = 120)
async def _():
    bot = nonebot.get_bot()
    try:
        api = twitter_get_api()

        last_id = ''
        try:
            last_id = get_last_id()
        except FileNotFoundError:
            print("Can't find last tweet information")
            last_id = None
        for ID in IDs:
            for status in tweepy.Cursor(api.user_timeline, id = ID, since_id = last_id, tweet_mode="extended").items(5):
                try:
                    msg = generatemsg(status)
                    strinfo = re.compile('\s')
                    dmsg = strinfo.sub(' ', status.full_text)
                    tslmsg = translate(dmsg)
                    if last_id != None:
                        for group_id in group_ids:
                            await bot.send_msg(group_id = group_id, message = msg)
                            await bot.send_msg(group_id = group_id, message = tslmsg)
                            await bot.send_msg(group_id = group_id, message = r'https://twitter.com/' + ID + r'/status/' + status.id_str)
                        for user_id in user_ids:
                            await bot.send_msg(user_id = user_id, message = msg)
                            await bot.send_msg(user_id = user_id, message = tslmsg)
                            await bot.send_msg(user_id = user_id, message = r'https://twitter.com/' + ID + r'/status/' + status.id_str)
                        # await bot.send_msg(group_id = 692510749, message = '复制上面链接到下面网址来烤推：' + r'https://tweet.wudifeixue.com/?template=/template/tamashoko.txt')
                    if status.id_str > last_id:
                        last_id = status.id_str
                        set_last_id(status.id_str)
                except Exception as e:
                    print('Some errors occured when processing tweet ' + status.id_str + ' as ', e)
    except Exception as e:
        print('Some errors occured when automatic posting tweets: ', e)

# Support functions defination

def generatemsg(status):
    message= status.user.name + '的新推文：\n' + status.full_text
    try:
        if status.entities['media'] != []:
            for media in status.extended_entities['media']:
                print('downloading..' + media['media_url'])
                filename = os.path.basename(media['media_url'])
                #request download
                r = requests.get(media['media_url'], proxies = ssr_proxies, timeout = 3)
                with open(os.path.join(image_cachepath, filename), 'wb') as fh:
                    for chunk in r.iter_content(1024 * 1024):
                        fh.write(chunk)
                print('downloaded ' + filename + '\n')
                message = message + "[CQ:image,file=%s]" % (filename)
        else:
            pass
    except:
        print("no media found or some error occurred.")
    print("generated message is: " + message)
    return message

def get_last_id():
    with open(last_id_cachepath, 'r') as fr:
        return fr.read()

def set_last_id(tweet_id):
    with open(last_id_cachepath, 'w') as fr:
        fr.write(str(tweet_id))