import ssl

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from utils import config


RDS_CERT_PATH = r"C:\Users\user\.yandex\RootCA.crt"
ssl_context = ssl.create_default_context(cafile=RDS_CERT_PATH)
ssl_context.verify_mode = ssl.CERT_REQUIRED

connect_args = {"ssl": ssl_context}

engine = create_async_engine(config.SA_URL, connect_args=connect_args)
DBSession: sessionmaker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
