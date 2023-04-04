# Задача 49. Создать телефонный справочник  возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться # в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или 
# фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os
from time import sleep

def add_person():
    last_name = input('Введите фамилию: ')  # 'Иванов'
    name = input('Введите имя: ')           # 'Иван'
    surname = input('Введите отчество: ')   #'Иванович'
    phone = input('Введите номер телефона: ') #'9784561230'
    data = open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'a', encoding='utf-8')
    data.writelines([last_name,' ',  name, ' ',  surname, ' ', phone, '\n']) # 1-й вар.
    #data.writelines([last_name + ' ',  name + ' ',  surname + ' ', phone]) #2-й вар.
    data.close()

def print_data():
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r', encoding='utf-8') as data:
        print(data.read())
        sleep(5)

def search():
    search_name = input('Введите данные: ')
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)
                sleep(5)

def load_data():
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in  text_data:
                    data.write(line)
                    
def del_person():
    del_name = input('Введите данные контакта, который хотите изменить: ')
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for line in d:
            if del_name in line:
                del d[d.index(line)]
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'w', encoding='utf-8') as data:    
        for line in d:
            data.write(line)    

def change_person():
    change_name = input('Введите данные контакта, который хотите изменить: ')
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for line in d:
            if change_name in line:
                del d[d.index(line)]
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'w', encoding='utf-8') as data:    
        for line in d:
            data.write(line) 
    with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'a', encoding='utf-8') as data:
        last_name = input('Введите новую фамилию: ')  
        name = input('Введите новое имя: ')           
        surname = input('Введите новое отчество: ')   
        phone = input('Введите новый номер телефона: ')     
        data.writelines([last_name,' ',  name, ' ',  surname, ' ', phone, '\n'])
  
def user_interface():
    os.system("cls")
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')
    user_input = input('Введите нужный вариант: ')
    while user_input != "7":
        if user_input == '1':
            add_person()
        elif user_input == '2':
            search()
        elif user_input == '3':
            load_data()
        elif user_input == '4':
            print_data()
        elif user_input == '5':
            del_person()
        elif user_input == '6':
            change_person()
        else:
            print("Вы ввели некорректный вариант. Попробуйте еще раз ")
        os.system("cls")
        print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удалить контакт
6 - изменить контакт
7 - выход''')
        user_input = input('Введите нужный вариант: ')


def main():
    user_interface()

if __name__ == "__main__":
    main()





# def del_person():
#     del_name = input('Введите данные контакта, который хотите изменить: ')
#     with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'r', encoding='utf-8') as data:
#         d = data.readlines()
#         for line in d:
#             if del_name in line:
#                 print(d.index(line))
#                 index = d.index(line)
#                 del d[d.index(line)]
                

#                 for el in d:
#                     print(el)
#     with open('C:\\Users\\nastyaduko\\Documents\\GeekBrains\\Testing\\Python\\Seminars\\Les_8_dop\\phonebook.txt', 'w', encoding='utf-8') as data:    
#         for line in d:
#             data.write(line + '\n')    
#                 # data.write(d)
#                 # print(type(d))
#         # data.close()  
# del_person()
