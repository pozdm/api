from db.core import DBSession


def open_session(function):
    async def wrapper(*args, **kwargs):
        async with DBSession() as session:
            return await function(session, *args, **kwargs)

    return wrapper