from sqlalchemy import select, func

from db.models import ChatsUsersCountModel
from db.session import open_session


@open_session
async def get_chats_stats_for_date(session, date: str) -> tuple[str: int] | None:
    query1 = select(
        func.count(ChatsUsersCountModel.chat_id.distinct())
    ).filter(
        ChatsUsersCountModel.users_count > 1
    ).filter(
        func.date_trunc('day', ChatsUsersCountModel.time) == date
    )

    query2 = select(
        func.sum(ChatsUsersCountModel.users_count)
    ).filter(
        ChatsUsersCountModel.users_count > 1
    ).filter(
        func.date_trunc('day', ChatsUsersCountModel.time) == date
    )

    query3 = select(
        func.sum(ChatsUsersCountModel.messages_count)
    ).filter(
        ChatsUsersCountModel.users_count > 1
    ).filter(
        func.date_trunc('day', ChatsUsersCountModel.time) == date
    )

    result1 = await session.execute(query1)
    result2 = await session.execute(query2)
    result3 = await session.execute(query3)

    result1 = result1.scalar()
    result2 = result2.scalar()
    result3 = result3.scalar()

    if not (result1 and result2 and result3):
        return None

    return {
        "chats": result1,
        "users": result2,
        "messages": result3
    }




