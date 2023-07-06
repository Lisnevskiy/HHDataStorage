-- Получает список всех компаний и количество вакансий у каждой компании.
SELECT employer, COUNT(*) FROM vacancies GROUP BY employer;

-- Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
SELECT employer, title, salary_from, salary_to, url FROM vacancies;

-- Получает среднюю зарплату по вакансиям.
SELECT AVG(salary_from) FROM vacancies;

-- Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
SELECT * FROM vacancies WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies);

-- Получает список всех вакансий, в названии которых содержатся слово, например “python”.
SELECT * FROM vacancies WHERE title LIKE '%python%';
