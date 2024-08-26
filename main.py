from sqlalchemy.orm import relationship

from database.first_db import FirstTable



FirstTable.second_tables = relationship('SecondTable', back_populates='first_table')