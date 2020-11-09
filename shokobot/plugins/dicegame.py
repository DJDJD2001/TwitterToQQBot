from nonebot import on_command, CommandSession

import random

__plugin_name__ = '骰娘'
__plugin_usage__ = r'''
格式：
骰娘+dice/骰子+1d100/1d6/1d...
'''

@on_command('dicegame', aliases = ('骰子', '色子', 'dice'))
async def dicegame(session: CommandSession):
    dice = session.get('dice')
    point = await random_point(dice)
    await session.send(str(point))


@dicegame.args_parser
async def _(session : CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if stripped_arg:
        if stripped_arg.find('d') != -1:
            if stripped_arg[0:stripped_arg.find('d')].isdigit() and stripped_arg[stripped_arg.find('d') + 1:].isdigit():
                session.state['dice'] = stripped_arg
            else:
                session.state['dice'] = '0d0'
        else:
            session.state['dice'] = '0d0'
    if not stripped_arg:
        session.state['dice'] = '1d6'


async def random_point(dice: str) -> str:
    if dice != '0d0':
        result = ''
        for i in range(0, int(dice[0:dice.find('d')])):
            result = result + str(random.randint(1, int(dice[dice.find('d')+1:]))) + ' '
        return result
    else:
        return '不支持的骰子类型' + dice + ' 默认1d6 ' + str(random.randint(1, 6))