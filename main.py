#from person_profile import Person_profile
from validator import Validator
from work_with_file import Read_file
import argparse


filename = 'D:\\documents\\01 - study\\5 семестр\\python_lab_2\\15.txt'


parser = argparse.ArgumentParser("Input & output path")
parser.add_argument("-read", type=str, default="15.txt", help="Read path")
parser.add_argument("-write", type=str, default="result.txt", help="Write path")
pars = parser.parse_args()
lines = Read_file(pars.read)
data = Validator(lines.array_list())
result = data.count_invalid_arguments()

print("Валидных записей:", result[0])
print("Невалидных записей:", result[1])
print("Некорректных указаний электронной почты: ", result[2])
print("Некорректных указаний роста: ", result[3])
print("Некорректных указаний ИНН: ", result[4])
print("Некорректных указаний номера паспорта: ", result[5])
print("Некорректных указаний университета: ", result[6])
print("Некорректных указаний возраста: ", result[7])
print("Некорректных указаний ученой степени: ", result[8])
print("Некорректных указаний мировоззрения: ", result[9])
print("Некорректных указаний адреса: ", result[10])




