from db import models
from . import config

from sqlalchemy import select, func

from db.models import Subscribers
from db.session import open_session


@open_session
async def subscriptions_to_notifications_period(session, start_date, end_date):
    query1 = select(
        Subscribers.tg, Subscribers.vk, Subscribers.total
    ).filter(
        func.date_trunc('day', Subscribers.time) == start_date
    )

    query2 = select(
        Subscribers.tg, Subscribers.vk, Subscribers.total
    ).filter(
        func.date_trunc('day', Subscribers.time) == end_date
    )

    result = await session.execute(query1)
    result = await session.execute(query2)



    return result.one()
