import requests

from constants import HH_VACANCY_URL


class HeadHunterAPI:
    """
    Класс для работы с API HeadHunter.
    """
    @staticmethod
    def get_vacancies_by_employers(employers: list, keyword=None) -> list:
        """Получение данных о вакансиях по ID работодателей с помощью API HeadHunter."""

        params = {'text': keyword,
                  'page': 0,
                  'per_page': 100,
                  'order_by': 'publication_time',
                  'area': 113,
                  'employer_id': employers,
                  'only_with_salary': True  # Показывать вакансии только с указанием зарплаты.
                  }

        response = []

        for page in range(20):
            params.update({'page': page})
            data = requests.get(HH_VACANCY_URL, params=params)
            response += data.json()['items']

        return response
