import sqlite3


class DataBase:
    def __init__(self, url='database.db'):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def __run_sql_query(self, sql_query):
        self.cursor.execute(sql_query)
        self.connection.commit()

    def create_table(self, data):
        table_name = data['table_name']
        sql_middle = ''
        for key, value in data['columns'].items():
            sql_middle += f"{key} {value},"

        sql_query = f"""create table if not exists {table_name}
        ({sql_middle[:-1]})"""
        self.__run_sql_query(sql_query=sql_query)

    def insert_values(self, data):
        for lecture in data:
            print(lecture)
            sql_query = f"""
            INSERT INTO lecture (subject, name, time)
            VALUES({lecture[0]},{lecture[1]},{lecture[2]});
            """
            self.__run_sql_query(sql_query)

    def close_connection(self):
        self.connection.close()


