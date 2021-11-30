import json
import person_profile


class Read_file:
    _filename: str
    _array: list = []

    def __init__(self, file_path: str) -> None:
        self._file_path = file_path
        data = json.load(open(self._file_path, encoding="windows-1251"))
        for i in data:
            self._array.append(person_profile)

    def array_list(self) -> list:
        return self._array.copy()
