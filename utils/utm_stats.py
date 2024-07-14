from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session


@open_session
async def get_utm_stats_for_date(session, date: str, developers: list = []) -> any:
    query = select(
        VKModel.utm_term, func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(developers)
    ).filter(
        VKModel.utm_term != None
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    ).group_by(
        VKModel.utm_term
    )

    result = await session.execute(query)
    result = result.all()

    res = {}
    res.update(result)

    if not res:
        return None

    return res
