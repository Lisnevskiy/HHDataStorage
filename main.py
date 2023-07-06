from config import config
from constants import EMPLOYERS, HEAD_HUNTER_DB
from src.utils import create_database, save_data_to_database
from src.db_manager import DBManager
from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def main():

    hh = HeadHunterAPI()
    api_response = hh.get_vacancies_by_employers(EMPLOYERS, 'it')

    vacancies = Vacancy.instantiate_from_hh_data(api_response)
    vacancies = [item.__dict__ for item in vacancies]

    params = config()

    create_database(HEAD_HUNTER_DB, params)

    save_data_to_database(vacancies, HEAD_HUNTER_DB, params)

    database = DBManager(HEAD_HUNTER_DB, params)

    print(database.get_companies_and_vacancies_count())
    print(database.get_all_vacancies())
    print(database.get_avg_salary())
    print(database.get_vacancies_with_higher_salary())
    print(database.get_vacancies_with_keyword('инженер'))


if __name__ == '__main__':
    main()
