from sqlalchemy import Column, Integer, String, Boolean
from db.db import Base


class DbTask(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String)
    description = Column(String)
    completed = Column(Boolean)
