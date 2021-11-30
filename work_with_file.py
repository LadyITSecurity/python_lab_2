import json
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


