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

    chats = await session.execute(query1)
    users = await session.execute(query2)
    messages = await session.execute(query3)

    chats = chats.scalar_one_or_none()
    users = users.scalar_one_or_none()
    messages = messages.scalar_one_or_none()

    if not (chats or users or messages):
        return None

    return {
        "chats": chats,
        "users": users,
        "messages": messages
    }




