import nonebot
from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

@on_command('usage')
async def _(session: CommandSession):

    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    
    # Message not include arguments
    if not arg:
        await session.send(
            '现在支持的功能有：\n' + '\n'.join(p.name for p in plugins)
        )
        return

    # Message include arguments
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)

@on_natural_language(keywords = {'帮助', '方法', '使用'})
async def _(session : NLPSession):
    
    return IntentCommand(80.0, 'usage')