import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import tweepy
from jieba import posseg
import cn2an

from shokobot.plugins.twitter import twitter_get_api
from shokobot.plugins.settings import twitter_id as IDs

__plugin_name__ = '查询推文'
__plugin_usage__ = r'''
使用例：bot，获取最近5条推文
或：bot，获取第三条推特
'''

ID = 'Tamashoko_'

# Get one tweet
@on_command('gettweet')
async def gettweet(session: CommandSession):
    print('processing \'gettweet\'')
    count = session.get('count')
    msg = generatemsg(count)
    await session.send(msg)

@gettweet.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['count'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('推文编号不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg

@on_natural_language(keywords = {'获取第', '推送第'})
async def _(session : NLPSession):
    stripped_msg = session.msg_text.strip()
    count = texttonum_1(stripped_msg)
    return IntentCommand(80.0, 'gettweet', current_arg = str(count) or '')

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

# Get couple of tweet
@on_command('gettweets')
async def gettweets(session: CommandSession):
    print('processing \'gettweets\'')
    count = session.get('count')
    msg = generatemsgs(count)
    await session.send(msg)

@gettweets.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        if stripped_arg:
            session.state['count'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('推文数量不能为空呢，请重新输入')
    session.state[session.current_key] = stripped_arg

@on_natural_language(keywords = {'获取最近', '推送最近'})
async def _(session : NLPSession):
    stripped_msg = session.msg_text.strip()
    count = texttonum_2(stripped_msg)
    return IntentCommand(80.0, 'gettweets', current_arg = str(count) or '')

# Support functions defination

def generatemsgs(count):
    api = twitter_get_api()
    msg = ''
    try:
        i = 1
        for status in tweepy.Cursor(api.user_timeline, id = ID, tweet_mode="extended").items(int(count)):
            msg = msg + '最近第%d条推特：\n' % (i) + status.full_text + '\n'
            i = i + 1
    except Exception as e:
        print('Some errors occured when manually generating message: ', e)
    return msg

# Support functions defination

def texttonum_1(text: str):
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

def texttonum_2(text: str):
    words = posseg.lcut(text)

    count = None

    for word in words:
        if word.flag == 'm':
            print ('numberword is ' + word.word)
            try:
                count = cn2an.cn2an(word.word, "smart")
            except:
                count = cn2an.cn2an(word.word[:-1], "smart")
            break
    return count