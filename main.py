import os
import sqlite3

from seeds import (seed_discipline, seed_grades, seed_groups, seed_students,
                   seed_teachers)
from Write_to_file_txt import record_data_in_txt, file_txt_exist


CONNECT_BD = "hw_6.bd"
folder_path_query = "query"
file_create_db_sql = 'create_db.sql'


def open_query(folder_path):
    filename = [
        filename for filename in os.listdir(folder_path) if filename.endswith(".sql")
    ]

    filename_sorted = sorted(filename, key=lambda i: int(i.split(".")[0].split("_")[1]))

    for f in filename_sorted:
        file_path = os.path.join(folder_path, f)

        with open(file_path, "r", encoding="utf-8") as file:
            sql_content = file.read()
            yield sql_content


def create_bd(cur, file_sql):
    with open(file_sql, 'r', encoding='utf-8') as f:
        create_bd_content = f.read()
        statements = create_bd_content.split(';')
        for statement in statements:
            statement = statement.strip()
            if statement:
                try:
                    cur.execute(statement)
                except sqlite3.Error as e:
                    print(f'Error executing statement: {e}')


if __name__ == "__main__":
    with sqlite3.connect(CONNECT_BD) as connect:
        cur = connect.cursor()

        try:
            create_bd(cur, file_create_db_sql)

            seed_teachers(cur)
            seed_discipline(cur)
            seed_groups(cur)
            seed_students(cur)
            seed_grades(cur)

            try:
                file_txt_exist()

                for i, query in enumerate(open_query(folder_path_query), 1):
                    print(f"Executing Query {i}: {query}")
                    record_data_in_txt(f"Executing Query {i}: {query}")
                    
                    result = cur.execute(query).fetchall()
                    print(f"Query {i} Result:", result)
                    print("=" * 50)
                    record_data_in_txt(f"Query {i} Result: {result}")
                    record_data_in_txt(f"=" * 50)
                    
            except sqlite3.Error as error:
                print(f"Error executing query {i}: {error}")

        except sqlite3.Error as error:
            print(f"Error: {error}")
