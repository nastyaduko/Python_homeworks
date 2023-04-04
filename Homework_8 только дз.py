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
del_person()


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
change_person()       
        
