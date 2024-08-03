import json
import psycopg2

with psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Shutka757'
) as conn:
    with conn.cursor() as cur:
        cur.execute("""
                CREATE TABLE vacancies (
                    company varchar (100),
                    job_title varchar(100),
                    link_to_vacancy varchar(100),
                    salary_from int,
                    salary_to int,
                    description text,
                    requirement text); 
                    """)  # создаём таблицу sql
        with open('vacancy_json.json', 'r', encoding='utf-8') as file:  # заполняем таблицу данными из созданного json-файла
            vacancies = json.load(file)
            for vacancy in vacancies:
                cur.execute(
                    'INSERT INTO vacancies (company, job_title, link_to_vacancy, salary_from, salary_to, '
                    'description, requirement) VALUES (%s, %s, %s, %s, %s, %s, %s)',
                    (vacancy.get('company'), vacancy.get('job_title'), vacancy.get('link_to_vacancy'),
                     vacancy.get('salary_from'), vacancy.get('salary_to'), vacancy.get('description'),
                     vacancy.get('requirement')))

        cur.execute("SELECT * FROM vacancies")
        rows = cur.fetchall()
        for row in rows:
            print(row)