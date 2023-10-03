import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, Uuid, Date, Enum
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///project.db')
Base = declarative_base()

class Projektas(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("pavadinimas", String)
    price = Column("kaina", Float)
    author = Column("author", String)
    amount = Column("amount", Float)
    rating = Column("rating", Float)

    created_date = Column("date of creation", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price, author, amount_of_copy, rating):
        self.name = name
        self.price = price
        self.author = author
        self.amount = amount_of_copy
        self.rating = rating

    def __repr__(self):
        return f"{self.id} {self.name} - {self.price}: {self.created_date}"

Base.metadata.create_all(engine)