from sqlalchemy import select, func

from db.models import VKModel
from db.session import open_session
from utils.config import DEVELOPERS


@open_session
async def get_utm_stats_for_date(session, date: str) -> dict | None:
    query = select(
        VKModel.utm_term, func.count(VKModel.user_id)
    ).filter(
        VKModel.user_id.not_in(DEVELOPERS)
    ).filter(
        VKModel.utm_term != None
    ).filter(
        func.date_trunc('day', VKModel.event_timestamp) == date
    ).group_by(
        VKModel.utm_term
    )

    result = await session.execute(query)
    result = result.all()
    result_dict = dict(result)

    if not result_dict:
        return None

    return result_dict
