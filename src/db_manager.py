import psycopg2


class DBManager:

    def __init__(self, dbname, user, password, host):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        query = """
        SELECT company, 
        COUNT(*) FROM vacancies
        GROUP BY company
        """
        self.cur.execute(query)
        return {row[0]: row[1] for row in self.cur.fetchall()}

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
        вакансию."""
        query = """
        SELECT job_title, company, salary_from, salary_to, link_to_vacancy FROM vacancies
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям."""
        query = """
        SELECT AVG(salary_from) FROM vacancies
        """
        self.cur.execute(query)
        result = self.cur.fetchone()
        return result[0] if result else None

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        query = """
        SELECT job_title, salary_from FROM vacancies
        WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
        query = """
                        SELECT * FROM vacancy_table
                        WHERE LOWER(job_title) LIKE %s
                        """
        self.cur.execute(query, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()

    def close_connection(self):
        self.cur.close()
        self.conn.close()