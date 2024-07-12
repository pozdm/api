from sqlalchemy import select, func

from db.models import Subscribers
from db.session import open_session


# @open_session
# async def