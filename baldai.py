from sqlalchemy import Column, Integer, String, create_engine, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///many2many_test.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

association_table = Table('association', Base.metadata,
    Column('baldas_id', Integer, ForeignKey('baldas.id')),
    Column('gamintojas_id', Integer, ForeignKey('gamintojas.id'))
)

class Baldas(Base):
    __tablename__ = "baldas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    baldo_pavadinimas = Column(String)
    gamintojai = relationship("Gamintojas", secondary=association_table, back_populates="baldai")

    def __init__(self, baldo_pavadinimas):
        self.baldo_pavadinimas = baldo_pavadinimas

    def __repr__(self):
        return f"{self.baldo_pavadinimas}"

class Gamintojas(Base):
    __tablename__ = "gamintojas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    baldo_id = Column(Integer, ForeignKey("baldas.id"))
    baldo_gamintojas = Column(String)
    baldai = relationship("Baldas", secondary=association_table, back_populates="gamintojai")


Base.metadata.create_all(engine)

class CRUD:
    def __init__(self):
        self.session = Session()

    def read_by_id(self, baldas_id):
