from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session
from utils.config import DEVELOPERS


@open_session
async def get_users_before_date(session, date: str) -> int:
    query = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) <= date
    )

    result = await session.execute(query)

    return result.scalar()


@open_session
async def get_users_for_date(session, date: str) -> int:
    query = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    result = await session.execute(query)

    return result.scalar()


@open_session
async def get_views_for_date(session, date: str) -> int:
    query = select(
        func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    result = await session.execute(query)

    return result.scalar()
