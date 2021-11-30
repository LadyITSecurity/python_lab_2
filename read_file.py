import json


# класс чтения данных из файла по заданному пути
class Read_file:
    _filename: str
    _array: list = []

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        data = json.load(open(self._file_path, encoding="windows-1251"))
        for i in data:
            self._array.append(i)

    def array_list(self) -> list:
        return self._array.copy()
