import sqlite3
from sqlite3 import OperationalError

db_url = "duomenu_baze.db"

sql_query_drop_table = "drop table if exists studentai"
sql_query_create_table = """
    create table if not exists studentai(
    vardas text,
    pavarde text,
    balai integer
    );
    """
with sqlite3.connect(db_url) as connection:
    cursor = connection.cursor()
    cursor.execute(sql_query_drop_table)
    cursor.execute(sql_query_create_table)

students = [
    ('Dainius', 'Dimsa', 10),
    ('Kotrina', 'Suliokaite', 10)
]

with sqlite3.connect(db_url) as connection:
    cursor = connection.cursor()
    for student in students:
        sql_query = f"""
        insert into studentai (vardas, pavarde, balai)
        VALUES ("{student[0]}","{student[1]}","{student[0]}")
        """
        cursor.execute(sql_query)
        # print(sql_query)
        try:
            connection.commit()
        except (OperationalError, TypeError):
            print("Kazkas")
            print(sql_query)
    sql_query = 'DELETE FROM studentai WHERE vardas ="Dainius";'
    cursor.execute(sql_query)















    import sqlite3
    from sqlite3 import OperationalError

    db_url = 'duomenu_baze.db'

    sql_query_drop_table = "drop table if exists studentai;"
    sql_query_create_table = """
    create table if not exists studentai(
    vardas text,
    pavarde text,
    balai integer
    );
    """

    with sqlite3.connect(db_url) as connection:
        cursor = connection.cursor()
        cursor.execute(sql_query_drop_table)
        cursor.execute(sql_query_create_table)

    students = [
        ('Dainius', 'Dimša', 10),
        ('Kotrina', 'Šuliokaitė', 10),
    ]

    with sqlite3.connect(db_url) as connection:
        cursor = connection.cursor()
        for student in students:
            sql_query = f"""
            INSERT INTO studentai (vardas, pavarde, balai)
            VALUES ("{student[0]}", "{student[1]}", {student[2]});
            """
            # print(sql_query)
            try:
                cursor.execute(sql_query)
            except OperationalError:
                print("kazkas nesigavo: ")
                print(sql_query)
        sql_query = 'DELETE FROM studentai WHERE vardas="Dainius";'
        cursor.execute(sql_query)

    with sqlite3.connect(db_url) as connection:
        cursor = connection.cursor()
        sql_query = f"""
        INSERT INTO studentai (vardas, pavarde, balai)
        VALUES"""
        for student in students:
            sql_query += f'("{student[0]}", "{student[1]}", {student[2]}),'

        sql_query = sql_query[:-1]
        sql_query += ';'
        cursor.execute(sql_query)

    # VALUES
    # ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
    # ('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
    # ('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');