import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import tweepy
from jieba import posseg
import cn2an
import re

from shokobot.plugins.twitter import twitter_get_api
from shokobot.plugins.settings import twitter_id as IDs
from shokobot.plugins.translate import translate

__plugin_name__ = '机翻推文'
__plugin_usage__ = r'''
使用例：bot，翻译第5条推文
'''
ID = 'Tamashoko_'

@on_command('translatetweet')
async def translatetweet(session: CommandSession):
    count = session.get('count')
    msg = generatemsg(count)
    strinfo = re.compile('\s')
    dmsg = strinfo.sub(' ', msg)
    await session.send(translate(dmsg))

@translatetweet.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['count'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('推文编号不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg

@on_natural_language(keywords = {'翻译第'})
async def _(session : NLPSession):
    stripped_msg = session.msg_text.strip()
    count = texttonum(stripped_msg)
    return IntentCommand(80.0, 'translatetweet', current_arg = str(count) or '')

# Support functions defination

def generatemsg(count):
    api = twitter_get_api()
    msg = ''
    try:
        for status in tweepy.Cursor(api.user_timeline, id = ID, tweet_mode="extended").items(int(count)):
            msg = status.full_text + '\n'
    except Exception as e:
        print('Some errors occured when manually generating message: ', e)
    return msg

def texttonum(text: str):
    words = posseg.lcut(text)

    count = None

    for word in words:
        if word.flag == 'm':
            print ('numberword is ' + word.word)
            try:
                count = cn2an.cn2an(word.word[1:], "smart")
            except:
                count = cn2an.cn2an(word.word[1:-1], "smart")
            break
    return count