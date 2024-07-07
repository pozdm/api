from db import models
from . import config

from sqlalchemy import select, func

from db.models import Subscribers
from db.session import open_session


def get_difference(value1: int, value2: int) -> str:
    difference = value1 - value2
    return f"+{difference}" if difference > 0 else f"{difference}"



