#  Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# (*) Усложнение. Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе

def get_user_data() -> list:
    name = input('Введите имя: ')
    sur_name = input('Введите фамилию: ')
    phone_num = input('Введите номер телефона: ')
    desc = input('Введите описание: ')
    return [name,sur_name,phone_num,desc]

def create_record(gb_phone_book: list, user_data: list) -> list:
    gb_phone_book.append(user_data)
    return gb_phone_book

def print_phone_book(gb_phone_book:list) -> None:
    for record in gb_phone_book:
        print(record)

def get_file_name() -> str:
    return input('Введите имя файла: ')

def create_from_data(gb_phone_book: list,file_name:str,delimiter:str ) -> list:
    path_sourse= os.path.join ('.',file_name)
    with open(path_sourse,'r', encoding='utf-8') as sourse:
        for line in sourse:
            gb_phone_book=create_record(gb_phone_book,line.strip().split(delimiter))
        return gb_phone_book

def menu():
    phone_book = list()
    while True:
        print('Введите 1 для выхода из справочника')
        print('Введите 2 для создания новой записи')
        print("Введите 3 для вывода на экран")
        print("Введите 4 для импорта данных из файла")
        choise = int(input('Ваш выбор: '))
        if choise == 1:
            print('Вы выбрали выход')
            return
        if choise == 2:
            phone_book = create_record(phone_book, get_user_data())
        if choise == 3:
            print_phone_book(phone_book)
        if choise==4:
            phone_book=create_from_data(phone_book,get_file_name(),',')
import os
menu()