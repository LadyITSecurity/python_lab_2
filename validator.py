from tqdm import tqdm
import re


# класс для проверки валидности данных, хранящий в себе данные о каждой ошибке и список экземпляров данных о людях
class Validator:
    _collection: list

    def __init__(self, data: list):
        self._collection = data

    def check_valiable_information(self, i: int) -> bool:
        if self.check_email(i) & self.check_height(i) & self.check_inn(i) & self.check_passport_number(i) & self.check_university(i) & self.check_age(i) & self.check_academic_degree(i) & self.check_worldview(i) & self.check_address(i):
            return True
        return False

    def check_email(self, i: int) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self._collection[i].get("email")):
            return True
        return False

    def check_height(self, i: int) -> bool:
        if isinstance(self._collection[i].get("height"), float):
            if 1.5 <= self._collection[i].get("height") <= 2.00:
                return True
            return False

    def check_inn(self, i: int) -> bool:
        if not re.match(r'\d{12}', self._collection[i].get("inn")):
            return True
        return False

    def check_passport_number(self, i: int) -> bool:
        if re.match(r'\d{6}', str(self._collection[i].get("passport_number"))):
            return True
        return False

    def check_university(self, i: int) -> bool:
        pattern = '([Уу]ниверситет| [Ии]нститут|[Aа]кадем|им. |[Пп]олитех|([А-Я]{3,}))+(\s|[а-я])'
        if re.match(pattern, self._collection[i]["university"]) is not None:
            return True
        return False

    def check_age(self, i: int) -> bool:
        if isinstance(self._collection[i].get("age"), int):
            if 20 <= self._collection[i].get("age") <= 80:
                return True
            return False

    def check_academic_degree(self, i: int) -> bool:
        pattern = 'Бакалавр|Специалист|Магистр|Кандидат наук|Доктор наук'
        if re.match(pattern, self._collection[i]["academic_degree"]) is not None:
            return True
        return False

    def check_worldview(self, i: int) -> bool:
        pattern = 'Христианство|Ислам|Буддизм|Иудаизм|Индуизм|Атеизм|Агностицизм|Деизм|Пантеизм|Католизм'
        if re.match(pattern, self._collection[i]["academic_degree"]) is not None:
            return True
        return False

    def check_address(self, i: int) -> bool:
        pattern = r"[а-яА-Я.\s\d-]+\s+[0-9]+$"
        if re.match(pattern, self._collection[i]["address"]) is not None:
            return True
        return False

    def count_invalid_arguments(self):

        count_of_error = 0
        wrong_email = 0
        wrong_height = 0
        wrong_inn = 0
        wrong_passport_number = 0
        wrong_university = 0
        wrong_age = 0
        wrong_academic_degree = 0
        wrong_worldview = 0
        wrong_address = 0
        result = []
        flag = False

        for i in tqdm(range(len(self._collection)),
                      desc="Проверка записей на коректность и получение статистики",
                      ncols=1000):
            if not self.check_email(i):
                wrong_email += 1
                flag = True
            if not self.check_height(i):
                wrong_height += 1
                flag = True
            if not self.check_inn(i):
                wrong_inn += 1
                flag = True
            if not self.check_passport_number(i):
                wrong_passport_number += 1
                flag = True
            if not self.check_university(i):
                wrong_university += 1
                flag = True
            if not self.check_age(i):
                wrong_age += 1
                flag = True
            if not self.check_academic_degree(i):
                wrong_academic_degree += 1
                flag = True
            if not self.check_worldview(i):
                wrong_worldview += 1
                flag = True
            if not self.check_address(i):
                wrong_address += 1
                flag = True
            if flag:
                count_of_error += 1
                flag = False

        result.append(len(self._collection))
        result.append(count_of_error)
        result.append(wrong_email)
        result.append(wrong_height)
        result.append(wrong_inn)
        result.append(wrong_passport_number)
        result.append(wrong_university)
        result.append(wrong_age)
        result.append(wrong_academic_degree)
        result.append(wrong_worldview)
        result.append(wrong_address)
        return result

