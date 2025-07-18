from sqlalchemy import Column, Integer, String

from app.database import Base


class Items(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True) # primary_key первичный коюч , последовательная генерация
    name = Column(String, nullable=False) # nullable поля должны быть заполнены
    description = Column(String, nullable=False)
    text = Column(String, nullable=False)
