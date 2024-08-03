# import psycopg2
#
#
# def create_db(name, params):
#     conn = psycopg2.connect(dbname='postgres', **params)
#     conn.autocommit = True
#     cur = conn.cursor()
#     cur.execute(f'DROP DATABASE IF EXISTS {name}')
#     cur.execute(f'CREATE DATABASE {name}')
#     with cur:
#         cur.execute("""CREATE TABLE employers ()""")
#     with cur:
#         cur.execute("""CREATE TABLE vacancies ()""")
#     conn.commit()
#     conn.close()