from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session


@open_session
async def total_unique_users_before_date(session, date: str, developers: list) -> int:
    query = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(developers)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) <= date
    )

    result = await session.execute(query)

    return result.scalar()


@open_session
async def unique_users_for_date(session, date: str, developers: list) -> int:
    query = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(developers)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    result = await session.execute(query)

    return result.scalar()


@open_session
async def views_for_date(session, date: str, developers: list) -> int:
    query = select(
        func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(developers)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    result = await session.execute(query)

    return result.scalar()
