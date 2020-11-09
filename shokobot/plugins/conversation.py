from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
import random
from jieba import posseg

__plugin_name__ = '对话'
__plugin_usage__ = r'''
最简单的对话功能，发挥您的想象力吧
'''

@on_command('conversation')
async def conversation(session: CommandSession):
    print('processing \'conversation\'')
    text = session.get('text', prompt = '干嘛')
    x = random.randint(1, 4)
    if x == 4:
        await session.send('[CQ:at,qq=%s] %s' % (session.ctx['user_id'], text))
    else:
        await session.send('[CQ:at,qq=%s] 不%s' % (session.ctx['user_id'], text))

@on_command('special_conversation')
async def special_conversation(session: CommandSession):
    print('processing \'special_conversation\'')
    x = random.randint(1, 10)
    if x == 10:
        await session.send('[CQ:at,qq=%s] %s' % (session.ctx['user_id'], '嗯'))
    else:
        await session.send('[CQ:at,qq=%s] %s' % (session.ctx['user_id'], '爬'))

@conversation.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    
    verb = select_verb(stripped_arg)
    
    if session.is_first_run:
        if stripped_arg:
            session.state['text'] = verb or '好'
        return

    if not stripped_arg:
        session.pause('?')

    session.state[session.current_key] = verb or '好'

@on_natural_language(keywords = {''})
async def _(session : NLPSession):

    stripped_msg = session.msg_text.strip()

    return IntentCommand(60.0, 'conversation', current_arg = select_verb(stripped_msg) or '')

@on_natural_language(keywords = {'rbq', 'RBQ', '开房', '做爱'})
async def _(session : NLPSession):
    return IntentCommand(61.0, 'special_conversation')

# Support functions defination

def select_verb(text: str):
    words = posseg.lcut(text)
    verb = None

    for word in words:
        if word.flag == 'v':
            verb = word.word
            break

    return verb