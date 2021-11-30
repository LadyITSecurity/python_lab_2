import json
from tqdm import tqdm
#import person_profile


class Read_file:
    _filename: str
    _array: list = []

    def __init__(self, filename: str) -> None:
        self._filename = filename
        data = json.load(open(self._filename, encoding="windows-1251"))
        for i in data:
            self._array.append(i)

    def array_list(self) -> list:
        return self._array.copy()


class Write_file:
    _filename: str

    def __init__(self, filename) -> None:
        self._filename = filename

    def write_file(self, collection: list) -> None:

        tmp = []
        for i in tqdm(range(collection.get_count_of_profile()), desc="Запись корректных данных в файл: ", ncols=100):
            if collection.check_valid_information(i):
                tmp.append(collection.get_profile(i))
        json.dump(tmp, open(self._filename, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)

