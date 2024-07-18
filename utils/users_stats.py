from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session
from utils.config import DEVELOPERS


@open_session
async def get_users_for_date(session, date: str) -> dict | None:
    query1 = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) <= date
    )

    query2 = select(
        func.count(VKModel.user_id.distinct())
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    query3 = select(
        func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    )

    total_users = await session.execute(query1)
    users_for_day = await session.execute(query2)
    views_for_day = await session.execute(query3)

    total_users = total_users.scalar_one_or_none()
    users_for_day = users_for_day.scalar_one_or_none()
    views_for_day = views_for_day.scalar_one_or_none()

    if not (total_users or users_for_day or views_for_day):
        return None

    return {
        "total_users": total_users,
        "users_for_day": users_for_day,
        "views_for_day": views_for_day
    }
