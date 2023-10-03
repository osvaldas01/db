import sqlite3

class DB:

    def __init__(self, url="new_db.db"):
        self.url = url


    def execute_query(self, data):
        with sqlite3.connect(self.url) as connection:
            cursor = connection.cursor()
            cursor.execute(data)

    def insert_values(self, students):
        with sqlite3.connect(self.url) as connection:
            cursor = connection.cursor()
            for student in students:
                sql_insert = f"""
                        INSERT INTO students (name, surname, mark)
                        VALUES ("{student[0]}", "{student[1]}", {student[2]});
                        """
                cursor.execute(sql_insert)

    def delete_rows(self, condition):
        delete_query = f'DELETE FROM students WHERE {condition};'
        self.execute_query(delete_query)

    def update_rows(self, old_data, new_data):
        update_query = f"""
            UPDATE students
            SET name = "{new_data[0]}", surname = "{new_data[1]}", mark = {new_data[2]}
            WHERE {old_data};
        """
        self.execute_query(update_query)

