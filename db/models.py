import json

from sqlalchemy import inspect, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from clickhouse_sqlalchemy import engines

from utils import config


__all__ = ("Base", "CheckModel")

Base = declarative_base()


class MixinSerializers:
    """should only be used as sa model base"""

    def to_python(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

    def as_json(self) -> str:
        return json.dumps(self.to_python(), indent=4)

    # def __str__(self):
    #     return f"<{self.__tablename__}(time={self.time}, app={self.app}, title={self.title}, link={self.link}, status={self.status})>"  # type: ignore

    def as_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class VKModel(MixinSerializers, Base):
    """?"""

    __tablename__ = config.VK
    __table_args__ = (
        engines.MergeTree(),
    )
    user_id = Column(Integer, primary_key=True, nullable=True)
    event_name = Column(String, nullable=True)
    event_type = Column(String, nullable=True)
    screen_name = Column(String, nullable=True)
    event_timestamp = Column(DateTime, nullable=True)
    json_data = Column(String, nullable=True)
    utm_campaign = Column(String, nullable=True)
    utm_source = Column(String, nullable=True)
    utm_term = Column(String, nullable=True)


class ChatsUsersCountModel(MixinSerializers, Base):
    """Статистика по количеству пользователей в чатах"""

    __tablename__ = config.CHATS_USERS_COUNT
    __table_args__ = (
        engines.TinyLog(),
    )
    measurement = Column(String, nullable=True)
    time = Column(DateTime, nullable=True)
    chat_id = Column(Integer, primary_key=True, nullable=True)
    users_count = Column(Integer, nullable=True)
    messages_count = Column(Integer, nullable=True)


class Subscribers(MixinSerializers, Base):
    """Количество пользователей vk/tg"""

    __tablename__ = 'users_subscribe_count'
    __table_args__ = (
        engines.Log(),
    )
    time = Column(DateTime, nullable=True, primary_key=True)
    total = Column(Integer, nullable=True)
    tg = Column(Integer, nullable=True)
    vk = Column(Integer, nullable=True)
