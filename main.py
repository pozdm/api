from datetime import datetime, timedelta
import asyncio

from utils import subscribers_stats


developers = []

today = (datetime.now().replace(hour=0, minute=0, second=0, microsecond=0))
last_day = (today - timedelta(days=1))
last_week = (today - timedelta(days=8))


async def main():
    result = await subscribers_stats.subscriptions_to_notifications_period(last_day, today)
    print(result)


# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())

print(type(datetime.now()))






