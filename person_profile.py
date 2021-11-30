import re


# экземпляр исходных данных, словарь данных об одном человеке, осуществляет проверку каждого поля
class Person_profile:
    _data: dict

    def __init__(self, data: dict):
        self._data = data.copy()

    def check_email(self) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self._data.get("email")):
            return True
        return False

    def check_height(self) -> bool:
        if isinstance(self._data.get("height"), float):
            if 1.5 <= self._data.get("height") <= 2.00:
                return True
            return False

    def check_inn(self) -> bool:
        if not re.match(r'\d{12}', self._data["inn"]):
            return True
        return False

    def check_passport_number(self) -> bool:
        if not re.match(r'\d{6}', self._data["passport_number"]):
            return True
        return False

    def check_university(self) -> bool:
        pattern = '([Уу]ниверситет| [Ии]нститут|[Aа]кадем|им. |[Пп]олитех|([А-Я]{3,}))+(\s|[а-я])'
        if re.match(pattern, self._data["university"]) is not None:
            return True
        return False

    def check_age(self) -> bool:
        if isinstance(self._data.get("age"), int):
            if 20 <= self._data.get("age") <= 80:
                return True
            return False

    def check_academic_degree(self):
        pattern = 'Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук'
        if re.match(pattern, self._data["academic_degree"]) is not None:
            return True
        return False

    def check_address(self):
        pattern = '(ул. ([А-Я]{1,}[а-я]))'
        if re.match(pattern, self._data["address"]) is not None:
            return True
        return False

