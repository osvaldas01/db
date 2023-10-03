from new import NewDB

table_creation = """
create table if not exists balamaba(
name TEXT,
age integer
salary integer)
"""

values = [
    ('Osvaldas', 22, 1500),
    ('Matas', 22, 1600),
]




db = NewDB()
db.execute_query(table_creation)
db.insert_values(values)