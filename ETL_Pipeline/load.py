import pandas as pd
import snowflake.connector
from config import credentials

class Load:
    def load(self, csv_file_path, schema, table):
        conn = snowflake.connector.connect(
            user=credentials["USER"],
            password=credentials["PASSWORD"],
            account=credentials["ACCOUNT"],
            warehouse=credentials["WAREHOUSE"],
            database=credentials["DATABASE"]
        )

        cur = conn.cursor()

        df = pd.read_csv(csv_file_path)
        cur.execute(f"USE SCHEMA {schema}")
        for row in df.itertuples():
            get_data = f"SELECT title FROM {table}"
            cur.execute(get_data)
            lst = cur.fetchall()
            titles = [title[0] for title in lst]
            if row[1] not in titles:
                sql_query = f'''
                INSERT INTO {table} (title, link, imgsrc)
                VALUES {row[1:4]}
                '''
                cur.execute(sql_query)

        print(f"Data appended to the table {schema}.{table} successfully")

