class Vacancy:

    def __init__(self, vid, name, url, employer, salary_from, salary_to, requirement, responsibility, area):
        """
        Конструктор класса Vacancy.

        :param vid: ID вакансии
        :param name: Название вакансии.
        :param url: Ссылка на вакансию.
        :param employer: Работодатель.
        :param salary_from: Минимальная зарплата.
        :param salary_to: Максимальная зарплата.
        :param requirement: Требования.
        :param responsibility: Обязанности.
        :param area: Город.
        """
        self.vid = vid
        self.name = name
        self.url = url
        self.employer = employer
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.requirement = requirement
        self.responsibility = responsibility
        self.area = area

    def __str__(self):
        return f'********************************\n'\
               f'{self.name}\n' \
               f'--------------------------------\n' \
               f'ID: {self.vid}\n' \
               f'{self.url}\n' \
               f'Работодатель: {self.employer}\n' \
               f'Зарплата от {self.salary_from}\n' \
               f'Зарплата до {self.salary_to}\n' \
               f'Требования: {self.requirement}\n' \
               f'Обязанности: {self.responsibility}\n' \
               f'Город: {self.area}\n'\
               f'********************************\n'

    @classmethod
    def instantiate_from_hh_data(cls, hh_data):
        """
        Создает список объектов класса Vacancy на основе данных о вакансиях из API hh.ru.

        :param hh_data: Список словарей с данными о вакансиях из API hh.ru.
        :return: Список объектов класса Vacancy.
        """
        vacancies_list = []

        for data in hh_data:
            if data['salary'] is None:
                salary_from = None
                salary_to = None
            else:
                salary_from = data["salary"]["from"] if data["salary"]["from"] else 0
                salary_to = data["salary"]["to"] if data["salary"]["to"] else 0

            vacancy = Vacancy(int(data['id']), data['name'], data['alternate_url'], data['employer']['name'],
                              salary_from, salary_to, data['snippet']['requirement'], data['snippet']['responsibility'],
                              data['area']['name'])

            vacancies_list.append(vacancy)

        return vacancies_list
