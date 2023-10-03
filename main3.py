from db.db_management import DB

db = DB()

students = [
    ('Dainius', 'Dimša', 10),
    ('Kotrina', 'Šuliokaitė', 10)
]

table_creation = """
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        surname TEXT,
        mark INTEGER
    );
"""

update_condition = 'name = "Dainius"'
new_student_data = ('Petras', 'UpdatedSurname', 99)

db.execute_query(table_creation)
db.insert_values(students)
db.update_rows(update_condition, new_student_data)
