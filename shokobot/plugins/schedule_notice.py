from datetime import datetime

import nonebot
import pytz

from shokobot.plugins.settings import group_ids

@nonebot.scheduler.scheduled_job('cron', hour='0')
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        for group_id in group_ids:
            await bot.send_msg(group_id = group_id,
                                message = f'现在{now.hour}点整啦，该睡啦')
    except Exception as e:
        print('Some errors occured when sending timely tips: ', e)