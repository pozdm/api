from datetime import datetime, timedelta
import asyncio
from pprint import pprint
import json
from utils.config import DEVELOPERS

from utils import subscribers_stats, general_stats, chats_stats, views_stats, utm_stats
from static.templates import stats_day_form


developers = []

today = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
last_day = (today - timedelta(days=1))
last_week = (today - timedelta(days=8))


async def main():
    result = await utm_stats.get_utm_stats_for_date("2024.07.14")
    result = sorted(result, key=lambda x: x[1], reverse=True)
    res = {}
    res.update(result)
    print(json.dumps(res, indent=4))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())


