class Vacans:
    __slots__=('title','firm_com', 'salary','url','description')

    def __init__(self,title,firm_com, salary,url,description):
        self.title = title
        self.firm_com = firm_com
        self.salary = self.__salary_valid(salary)
        self.url =url
        self.description = description

    def __salary_valid(self,salary):
        if salary and salary["from"] is not None and salary["to"] is not None:
            return salary["from"] + (salary["to"] - salary["from"]) / 2
        elif salary and salary["from"] is not None:
            return  salary["from"]
        elif salary and salary["to"] is not None:
            return  salary["to"]
        else:
            return 0


    def __lt__(self, other):
        return self.salary < other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def to_dict(self):
        return {
            'title': self.title,
            'firm_com': self.firm_com,
            'salary':self.salary,
            'url':self.url,
            'description': self.description


        }

