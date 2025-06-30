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
            vacanci = file_headler.get_vacancy()
            for vacan in vacanci:
                if vacan['salary'] == 'Зарплата не указана':
                    print(vacan['salary'])


            # sorted_vacan = sorted(vacanci, key=lambda x: x.get("salary", 0), reverse=True)[:n]
            # if sorted_vacan:
            #     for vacancy in sorted_vacan:
            #         print(
            #             f"""
            #                 Навзание: {vacancy['name']},
            #                 Компания: {vacancy['employer']['name']},
            #                 Зарплата: {vacancy['salary']},
            #                 Ссылка: {vacancy['alternate_url']},
            #                 id: {vacancy['id']}
            #           """
            #         )
            # else:
            #     print("Вакансия не найдена")
        elif gert == "100":
            print("Выход из программы")
            break
