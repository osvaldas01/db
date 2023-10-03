from new_db import DataBase


table = {
    'table_name': 'lecture',
    'columns': {
    'subject': 'text',
    'name': 'text',
    'time': 'integer',
    }
}

lecture_data = [
    ('Vadyba', 'Domantas', 40),
    ('Python', 'Donatas', 80),
    ('Java', 'Tomas', 80)
]


db = DataBase()
# db.create_table(data=table)
db.insert_values(lecture_data)
db.close_connection()

# VALUES
# ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
# ('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
# ('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
# •Sukurti programą, kuri:
# •Sukurtų duomenų bazę
# •Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# •Sukurtų tris paskaitas: ('Vadyba', 'Domantas', 40),
# ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80)
# •Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 50
# •Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# •Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# •Atspausdintų visas paskaitas (visą lentelę)