import json
from datetime import datetime, timedelta
import asyncio
from pprint import pprint
from utils.config import DEVELOPERS

from utils import subscribers_stats, users_stats, chats_stats, views_stats, utm_stats
from api.statistics_api import return_json


developers = []

today = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
last_day = (today - timedelta(days=1))
last_week = (today - timedelta(days=8))


# x = {
#     "x": 1,
#     "y": 1
# }
# y = {
#     "x": 1,
#     "a": 1,
#     "b": 1
# }


async def main():
    chats_for_start_date = await chats_stats.get_chats_stats_for_date("2024-07-16")
    chats_for_end_date = await chats_stats.get_chats_stats_for_date("2024-07-17")
    print(return_json(chats_for_start_date, chats_for_end_date))


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())

# print(json.dumps(return_json(x, y), indent=4))


