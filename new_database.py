import sqlite3

class DataBase:

    def __init__(self, url="new_database.db"):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()


    def execute_query(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def insert_values(self, data):
            for lecture in data:
                sql_insert = f"""
                        INSERT INTO lecture (subject, name, time)
                        VALUES ("{lecture[0]}", "{lecture[1]}", {lecture[2]});
                        """
                self.execute_query(sql_insert)

    def get_data(self, sql_query):
        return self.cursor.execute(sql_query).fetchall()

    def update_rows(self, old_data, new_data):
        sql_query = f"""
    update lecture 
    set subject = "{new_data[0]}", name = "{new_data[1]}", time = "{new_data[2]}"
    where {old_data};
    """
        self.execute_query(sql_query)

    def delete_rows(self, condition):
        for key,value in condition.items():
            print(key, value)
            sql_query += f'key'
        # delete_query = f'delete from lecture where {condition};'
        # self.execute_query(delete_query)

    def print_whole_table(self, sql_query):
        return self.cursor.execute(sql_query).fetchall()