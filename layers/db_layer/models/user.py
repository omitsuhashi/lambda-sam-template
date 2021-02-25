from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from setting import Base


class Users(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)

    def __init__(self, name: str):
        self.name = name
