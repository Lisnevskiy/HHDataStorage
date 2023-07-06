from typing import Any

import psycopg2


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблицы для сохранения данных о вакансиях."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f'DROP DATABASE {database_name}')
    cur.execute(f'CREATE DATABASE {database_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                id SERIAL PRIMARY KEY,
                vac_id_head_hunter INTEGER,
                title VARCHAR(250) NOT NULL,
                url TEXT,
                employer VARCHAR(250),
                salary_from INTEGER,
                salary_to INTEGER,
                requirement TEXT,
                responsibility TEXT,
                area VARCHAR(100)
            )
        """)

    conn.commit()
    conn.close()


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict):
    """
    Сохранение данных о работодателях и вакансиях в базу данных.
    """
    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        for item in data:
            cur.execute("""INSERT INTO vacancies 
            (vac_id_head_hunter, title, url, employer, salary_from, salary_to, requirement, responsibility, area) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", tuple(item.values()))

    conn.commit()
    conn.close()
