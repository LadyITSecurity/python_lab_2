from tqdm import tqdm
import re


# класс для проверки валидности данных, хранящий в себе данные о каждой ошибке и список экземпляров данных о людях
class Validator:
    _collection: list

    def __init__(self, data: list):
        self._collection = data

    def get_profile(self, i: int) -> dict:
        return (self._collection[i]).copy()

    def get_count_of_profile(self) -> int:
        return len(self._collection)

    def check_valid_information(self, i: int) -> bool:
        if self.check_email(i) \
                and self.check_height(i) \
                and self.check_inn(i) \
                and self.check_passport_number(i) \
                and self.check_university(i) \
                and self.check_age(i) \
                and self.check_academic_degree(i) \
                and self.check_worldview(i) \
                and self.check_address(i):
            return True
        return False

    def check_email(self, i: int) -> bool:
        pattern = "^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self._collection[i].get("email")):
            return True
        return False

    def check_height(self, i: int) -> bool:
        if re.match(r'\d.\d{2}', self._collection[i].get("inn")):
            return True
        return False

    def check_inn(self, i: int) -> bool:
        if re.match(r'\d{12}', self._collection[i].get("inn")):
            return True
        return False

    def check_passport_number(self, i: int) -> bool:
        if isinstance(self._collection[i].get("passport_number"), int):
            if 0 <= self._collection[i].get("passport_number") <= 999999:
                return True
            return False

    def check_university(self, i: int) -> bool:
        pattern = '[Уу]ниверситет| [Ии]нститут|[Aа]кадем|им. |[Пп]олитех|'
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
        pattern = 'Христианство|Ислам|Буддизм|Иудаизм|Индуизм|Атеизм|Агностицизм|Конфуцианство|Деизм|Пантеизм|Католизм|Секулярный гуманизм'
        if re.match(pattern, self._collection[i]["worldview"]) is not None:
            return True
        return False

    def check_address(self, i: int) -> bool:
        pattern = r"[а-яА-Я.\s\d-]+\s+[0-9]+$"
        if re.match(pattern, self._collection[i]["address"]) is not None:
            return True
        return False

    def count_invalid_arguments(self) -> list:

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
                      desc="Проверка корректности данных:",
                      ncols=200):
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

        result.append(len(self._collection)-count_of_error)
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

    @property
    def collection(self):
        return self._collection

