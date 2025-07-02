from src.fileheander import JsonFileHendler
from src.hh_api import hh_API
from pprint import pprint

if __name__ == "__main__":
    hh_api = hh_API()
    file_headler = JsonFileHendler()

    while True:
        print(
            """Выберите дейсвие
        1. Поиск вакансий по ключевому слову
        2. Получить топ N вакансий по зарплате
        3. Получить вакансиис ключевым словом из файла
        4. Запись вакансий в файл
        100 выход из программы"""
        )

        gert = input("Введите действие:")
        if gert == "1":
            keyword = input("Введите словов для поиска: ")
            page = int(input("Введите кол-во вакансий поиска: "))
            page1 = int(input("Введите код региона, принаписании 0, будет приниматься регион Москвы: "))
            if page1 == 0:
                page1 = 113

            vacancies = hh_api.get_vacancion(keyword, page)
            try:
                for vacan in vacancies:
                    salary = vacan["salary"]
                    if salary and salary["from"] is not None and salary["to"] is not None:
                        aver_salary = salary["from"] + (salary["to"] - salary["from"]) / 2
                    elif salary and salary["from"] is not None:
                        aver_salary = salary["from"]
                    elif salary and salary["to"] is not None:
                        aver_salary = salary["to"]
                    else:
                        aver_salary = 0

                    pprint(
                        f"Название вакансии: {vacan['name']},"
                        f"Работодатель: {vacan['company']}, "
                        f"Ссылка:{vacan['url']} "
                        f"Средняя зарпалата: {vacan['salary']}"
                        f"id: {vacan['id']}"
                    )
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        elif gert == "2":
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
        elif gert == "3":
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
        elif gert == "4":

        elif gert == "100":
            print("Выход из программы")
            break
