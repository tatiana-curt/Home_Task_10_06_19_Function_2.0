# Задача 1. Создать класс Contact

class Contact:
    def __init__(self, first_name, last_name, phone, favored=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.kwargs = kwargs
        if favored == False:
            self.favored = 'нет'
        else:
            self.favored = 'да'

    def __str__(self):
        kwargs_list = '\n\t'.join(': '.join(v for v in k) for k in self.kwargs.items())
        return f'Имя: {self.first_name}\n' \
        f'Фамилия: {self.last_name}\n' \
        f'Телефон: {self.phone}\n' \
        f'В избранных: {self.favored}\n' \
        f'Дополнительная информация:\n\t{kwargs_list}'


jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
print(jhon)


# Задача 2. Создать класс PhoneBook

class PhoneBook(Contact):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.kwargs = kwargs
        self.number = 1
        print(kwargs)

    def print_contacts(self):
        for info in self.kwargs.values():
            print(info)

    def add_new_contact(self, first_name, last_name, phone, favored, *args, **kwargs):
        new_contact = Contact(first_name, last_name, phone, favored, *args, **kwargs)
        self.kwargs[self.number] = new_contact
        self.number += 1
        return self

    def remove_contact_by_phone(self, input):
        for key, info in list(self.kwargs.items()):
            if info.phone == input:
                del self.kwargs[key]
        return self

    def search_for_favored_contact(self):
        for info in self.kwargs.values():
            if info.favored == 'да':
                print(info)

    def search_for_contact_by_names(self, input):
        full_name = input.split(' ')
        for info in self.kwargs.values():
            if info.first_name == full_name[0] and info.last_name == full_name[1]:
                print(info)


def main():
    while True:
        user_input = input('Введите команду:\n'
                           '1 - напечатать список контактов;\n'
                           '2 - добавить новый контакт;\n'
                           '3 - удалить контакт по номеру телефона;\n'
                           '4 - вывести все избранные номера;\n'
                           '5 - найти контакт по имени и фамилии;\n'
                           'q - выйти\n')
        if user_input == '1':
            phones.print_contacts()
        elif user_input == '2':
            first_name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            phone = input('Введите номер телефона: ')

            favored = input('Является ли контакт избранным (необязательно): ')
            if favored == 'да':
                favored = True
            else:
                favored = False

            info_dict = {}
            additional_info = input('Введите дополнительные контактные данные через ":" (необязательно): ')
            if additional_info:
                if ', ' in additional_info:
                    resource = additional_info.split(', ')
                else: resource = [additional_info]
                for item in resource:
                    element = item.split(': ')
                    info_dict[element[0]] = element[1]

            phones.add_new_contact(first_name, last_name, phone, favored, **info_dict)
        elif user_input == '3':
            user_input = input('Введите номер телефона, чьей контакт нужно удалить: ')
            phones.remove_contact_by_phone(user_input)
        elif user_input == '4':
            phones.search_for_favored_contact()
        elif user_input == '5':
            user_input = input('Введите имя и фамилию через пробел: ')
            phones.search_for_contact_by_names(user_input)
        elif user_input == 'q':
            break
        else:
            print('Неверная команда')


# if __name__ == '__main__':
    # phones = PhoneBook(1, jhon=jhon)
    # main()