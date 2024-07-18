from sqlalchemy import select, func

from db.models import Subscribers
from db.session import open_session


@open_session
async def get_subscriptions_for_date(session, date: str) -> dict[str: int] | None:
    query = select(
        Subscribers.tg, Subscribers.vk, Subscribers.total
    ).filter(
        func.date_trunc('day', Subscribers.time) == date
    ).order_by(
        Subscribers.time.desc()
    ).limit(1)

    result = await session.execute(query)
    result = result.one_or_none()

    if result is None:
        return result

    return {
        "total": result[2],
        "tg": result[0],
        "vk": result[1]
    }
