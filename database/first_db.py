from database.base import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker


class FirstTable(Base):
    __tablename__ = 'first_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_id = Column(Integer, unique=True, nullable=False)
    description = Column(String(255))
    