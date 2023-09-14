from sqlalchemy import URL, create_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.core.config import get_settings

settings = get_settings()

# async_engine = create_async_engine(
#     URL.create("mysql+aiomysql", "root", "zzp949389", "localhost", 3306, "mysql"), pool_recycle=1500
# )
#
# AsyncSessionLocal = async_sessionmaker(async_engine, class_=AsyncSession)

engine = create_engine(
    URL.create("mysql+aiomysql", "root", "zzp949389", "localhost", 3306, "mysql"), pool_recycle=1500
)

SessionLocal = sessionmaker(engine)
