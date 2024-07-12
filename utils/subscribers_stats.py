from sqlalchemy import select, func

from db.models import Subscribers
from db.session import open_session


@open_session
async def get_subscriptions_for_date(session, date: str) -> tuple[int] | None:
    query = select(
        Subscribers.tg, Subscribers.vk, Subscribers.total
    ).filter(
        func.date_trunc('day', Subscribers.time) == date
    ).order_by(
        Subscribers.time.desc()
    ).limit(1)

    result1 = await session.execute(query)

    return result1.one_or_none()
