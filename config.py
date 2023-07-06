from configparser import ConfigParser


def config(filename="database.ini", section="postgresql"):
    """
    Функция для чтения конфигурационного файла database.ini и возврата параметров базы данных.

    :param filename: имя файла конфигурации (по умолчанию "database.ini").
    :param section: имя раздела в файле конфигурации (по умолчанию "postgresql").
    :return: словарь с параметрами базы данных.
    """
    # Создание парсера
    parser = ConfigParser()
    # Чтение файла конфигурации
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    return db
