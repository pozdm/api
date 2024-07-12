from datetime import datetime, timedelta
import asyncio
from pprint import pprint

from utils import subscribers_stats, general_stats, chats_stats, views_stats, utm_stats


developers = []

today = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
last_day = (today - timedelta(days=1))
last_week = (today - timedelta(days=8))


async def main():
    result = await views_stats.get_views_by_services("2024.07.10")
    pprint(result)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

