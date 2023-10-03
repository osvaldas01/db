from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///many2one_test.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class UnikalusGamintojas(Base):
    __tablename__ = "unikalus_gamintojai"
    id = Column(Integer, primary_key=True)
    baldo_gamintojas = Column("baldo gamintojas", String, unique=True)
    baldai = relationship("Baldas", back_populates="unikalus_gamintojas")

class Baldas(Base):
    __tablename__ = "baldas"
    id = Column(Integer, primary_key=True)
    baldo_pavadinimas = Column("Baldo Pavadinimas", String)
    gamintojas_id = Column(Integer, ForeignKey('unikalus_gamintojai.id'))
    unikalus_gamintojas = relationship("UnikalusGamintojas", back_populates="baldai")

# Base.metadata.create_all(engine)

class CRUD:
    def __init__(self):
        self.session = Session()

    def create_baldas(self, baldo_pavadinimas, gamintojas):
        unikalus_gamintojas = self.session.query(UnikalusGamintojas).filter_by(baldo_gamintojas=gamintojas).first()
        if not unikalus_gamintojas:
            unikalus_gamintojas = UnikalusGamintojas(baldo_gamintojas=gamintojas)
            self.session.add(unikalus_gamintojas)
            self.session.commit()

        baldas = Baldas(baldo_pavadinimas=baldo_pavadinimas, unikalus_gamintojas=unikalus_gamintojas)
        self.session.add(baldas)
        self.session.commit()

    def read_by_id(self, baldas_id):
        baldai = self.session.query(Baldas).filter_by(id=baldas_id).first()
        if baldai:
            print(baldai.baldo_pavadinimas, baldai.unikalus_gamintojas.baldo_gamintojas)
        else:
            print(f"Baldo su ID {baldas_id} nerastas")

crud = CRUD()
# crud.create_baldas("Lempa", "JYSK")
# crud.create_baldas("Stalas", "JYSK")
crud.read_by_id(2)
crud.read_by_id(4)


