import sqlite3


class NewDB:
    def __init__(self, url="NewDB.db"):
        self.url = url
        self.connection = sqlite3.connect(self.url)
        self.cursor = self.connection.cursor()

    def execute_query(self, sql_query):
        self.connection.execute(sql_query)
        self.connection.commit()

    def insert_values(self, data):
        for thing in data:
            sql_insert = f"""
            insert into balamaba(name, age, salary)
            values {thing[0]},{thing[1]},{thing[2]}
            """
        self.execute_query(sql_insert)
