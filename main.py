from datetime import datetime, timedelta
import asyncio
from pprint import pprint
import json

from utils import subscribers_stats, general_stats, chats_stats, views_stats, utm_stats
from static.templates import stats_day_form


developers = []

today = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
last_day = (today - timedelta(days=1))
last_week = (today - timedelta(days=8))


async def main():
    result = await general_stats.get_users_before_date("2024.07.16")
    pprint(result)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())



