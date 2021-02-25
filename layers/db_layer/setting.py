from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user_name = 'root'
password = 'root'
host = '127.0.0.1:8002'
db_name = 'resthub'

DATABASE = f'mysql://{user_name}:{password}@{host}/{db_name}?charset=utf8'

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=False,
)

# Sessionの作成
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=ENGINE,
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()
