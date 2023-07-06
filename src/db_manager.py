import psycopg2


class DBManager:
    def __init__(self, database_name: str, params: dict):
        """
        Конструктор класса DBManager.

        :param database_name: Имя базы данных.
        :param params: Параметры подключения к базе данных.
        """
        self.database_name = database_name
        self.params = params

    def get_connection(self):
        """
        Возвращает соединение с базой данных.
        :return: Объект соединения с базой данных.
        """
        return psycopg2.connect(dbname=self.database_name, **self.params)

    def get_companies_and_vacancies_count(self) -> list:
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("SELECT employer, COUNT(*) FROM vacancies GROUP BY employer")
            companies_and_vacancies_count = cur.fetchall()

        conn.close()

        return companies_and_vacancies_count

    def get_all_vacancies(self) -> list:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("SELECT employer, title, salary_from, salary_to, url FROM vacancies")
            all_vacancies = cur.fetchall()

        conn.close()

        return all_vacancies

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("SELECT AVG(salary_from) FROM vacancies")
            avg_salary = cur.fetchall()

        conn.close()

        return avg_salary[0][0]

    def get_vacancies_with_higher_salary(self) -> list:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)")
            vacancies_with_higher_salary = cur.fetchall()

        conn.close()

        return vacancies_with_higher_salary

    def get_vacancies_with_keyword(self, keyword: str) -> list:
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        """
        conn = self.get_connection()

        with conn.cursor() as cur:
            cur.execute("SELECT * FROM vacancies WHERE title LIKE %s", (f"%{keyword}%",))
            vacancies_with_keyword = cur.fetchall()

        conn.close()

        return vacancies_with_keyword
