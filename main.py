from src.fileheander import JsonFileHendler
from src.hh_api import hh_API
from pprint import pprint
from src.vacancies import Vacans

if __name__ == "__main__":
    hh_api = hh_API()
    keyword = input("Введите ключевое слово для поиска вакансий: ")
    count = int(input("Введите количество вакансий для поиска: "))
    area = input("Введите код региона (0 для Москвы): ")
    if area == 0:
        area = 113


    vacancies = hh_api.get_vacancion(keyword, count,area)
    try:
        vacancies_list = []
        for vacan in vacancies:
            vacancies_list.append(Vacans(vacan['name'],vacan['company'],vacan['salary'],vacan['url'],vacan['description']))
            salary = vacan["salary"]
    except Exception as e:
        print(f"Произошла ошибка: {e}")

    file_headler = JsonFileHendler()
    for v in vacancies_list:
        file_headler.add_vacancy(v.to_dict())

    while True:
            n = int(input("Введите N кол-во вакансий для получения: "))
            vacancy = file_headler.get_vacancy()
            sorted_vacan =[vacan for vacan in vacancy if vacan['salary'] == 'Зарплата не указана']
            sorted_vacan = sorted(sorted_vacan, key=lambda x: x.get("salary", 0), reverse=True)[:n]
            if sorted_vacan:
                for vacancys in sorted_vacan:
                    print(
                        f"""
                            Навзание: {vacancys['name']},
                            Компания: {vacancys['employer']['name']},
                            Зарплата: {vacancys['salary']},
                            Ссылка: {vacancys['alternate_url']},
                            id: {vacancys['id']}
                      """
                    )
            else:
                print("Вакансия не найдена")

            keywird = input("Введите ключевое слово: ")
            vacancy = file_headler.get_vacancy(name=keywird)
            if vacancy:
                for vacancys in vacancy:
                    print(
                        f"""
                            Навзание: {vacancys['name']},
                            Компания: {vacancys['employer']['name']},
                            Зарплата: {vacancys['salary']},
                            Ссылка: {vacancys['alternate_url']},
                            id: {vacancys['id']}
                      """
                    )
            else:
                print("Вакансия не найдена")

            break
