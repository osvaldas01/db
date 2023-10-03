from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from baldai import Baldas, Gamintojas, Base, association_table

engine = create_engine('sqlite:///many2many_test.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def add_new_baldas_gamintojas(baldo_pavadinimas, gamintojo_pavadinimas):
    naujas_baldas = Baldas(baldo_pavadinimas=baldo_pavadinimas)
    naujas_gamintojas = Gamintojas(baldo_gamintojas=gamintojo_pavadinimas)
    baldo_id = Baldas(baldo)
    naujas_baldas.gamintojai.append(naujas_gamintojas)
    session.add(naujas_baldas)
    session.add(naujas_gamintojas)
    session.commit()

class CRUD:
    def __init__(self):
        self.session = Session()

    def get_all(self):
        query = self.session.query(Baldas.baldo_pavadinimas, Gamintojas.baldo_gamintojas)
        result = query.all()
        print(result)

    def get_by_id(self, baldo_id):
        query = (
            self.session.query(Baldas.baldo_pavadinimas, Gamintojas.baldo_gamintojas)
            .join(Gamintojas, Gamintojas.baldo_id == Baldas.id)
            .filter(Baldas.id)
        )
        result = query.first()
        if result:
            print(result)
        else:
            print(f'Baldo su ID {baldo_id} nerasta.')


crud = CRUD()
# crud.get_all()
crud.get_by_id(1)


add_new_baldas_gamintojas("Sofa", "Ikea")
