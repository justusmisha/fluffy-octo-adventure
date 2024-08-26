from database.base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

from database.first_db import FirstTable


class SecondTable(Base):
    __tablename__ = 'second_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    transaction_id = Column(Integer, ForeignKey('first_table.transaction_id'))
    description = Column(String(255))
    first_table = relationship('FirstTable', back_populates='second_tables')

