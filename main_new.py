from new_database import DataBase


lecture_data = [
    ('Vadyba', 'Domantas', 40),
    ('Python', 'Donatas', 80),
    ('Java', 'Tomas', 80)
]

table_creation = """
    CREATE TABLE IF NOT EXISTS lecture (
        subject TEXT,
        name TEXT,
        time INTEGER
    );
"""
sql = '''
select *
from lecture
where time >= 50
'''

sql_table = '''
select * 
from lecture
'''

update_condition = 'subject = "Python"'
update_new = ('Python progromavimas', 'Donatas', 80)
delete_condition = 'name = "Tomas"'

db = DataBase()
# db.execute_query(table_creation)
db.insert_values(lecture_data)
# values = db.get_data(sql)
# print(values)
# db.update_rows(update_condition, update_new)
# db.delete_rows(delete_condition)
# whole_table = db.print_whole_table(sql_table)
# print(whole_table)