

class Contact:
    def __init__(self, name, surname, phone, elected=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.elected = elected
        self.kwargs = kwargs
        self.dict = {'Имя': self.name,
                     'Фамилия': self.surname,
                     'Телефон': self.phone,
                     'В избранных': self.elected,
                     'Дополнительная информация': self.kwargs}

    def print_dict(self):
        for item in self.dict:
            if item == 'Дополнительная информация':
                print('Дополнительная информация:')
                for item_2 in self.dict[item]:
                    yield ('         ') + str(item_2) + (': ') + str(self.dict[item][item_2])
            else:
                yield str(item) + (': ') + str(self.dict[item])

    def __str__(self):
        for item in self.print_dict():
            print(item)

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')

try:
    print(jhon)
except TypeError as e:
    pass

# _________________2 Задача_______________________
#

contact_list = [Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com'),
                Contact('Anna', 'Smith', '+71234567805', telegram='@Anna', email='Anna@smith.com'),
                Contact('Natali', 'Smith', '+71234567806', telegram='@Natali', email='Natali@smith.com'),
                Contact('Mari', 'Smith', '+71234567801', telegram='@Mari', email='Mari@smith.com')]

class PhoneBook(Contact):

    def __init__(self,  *args, **kwargs):
        self.kwargs = kwargs
        self.name_book = args

    def print_contact(self):
        for info in self.kwargs.values():
            try:
                print(info)
            except TypeError as e:
                pass

    def add_new_contact(self, name, surname, phone, elected=False, *args, **kwargs):
        new_contact = Contact(name, surname, phone, elected, *args, **kwargs)
        return new_contact

    def remove_contact(self, input):
        for key, info in list(self.kwargs.items()):
            if info.phone == input:
                del self.kwargs[key]
        return self

    def search_elected(self):
        for info in self.kwargs.values():
            if info.elected == True:
                try:
                    print(info)
                except TypeError as e:
                    pass

    def search_for_contact_by_names(self, input):
        for info in self.kwargs.values():
            if info.name == input[0] and info.surname == input[1]:
                try:
                    print(info)
                except TypeError as e:
                    pass


def main():
    phones_list = []
    for contact in contact_list:
        phone = PhoneBook('Mari_contact_book', contact=contact)
        phones_list.append(phone)
    while True:
        user_input = input('Введите команду:\n'
                           '1 - вывод списка;\n'
                           '2 - добавить новый контакт;\n'
                           '3 - удалить контакт по номеру телефона;\n'
                           '4 - вывести все избранные номера;\n'
                           '5 - найти контакт по имени и фамилии;\n'
                           'q - выйти\n')
        if user_input == '1':
            for phone in phones_list:
                phone.print_contact()
        elif user_input == '2':
            first_name = input('Введите имя: ')
            last_name = input('Введите фамилию: ')
            phone = input('Введите номер телефона: ')
            elected = input('Является ли контакт избранным (да или нет) (необязательно): ')
            if elected == 'да':
                elected = True
            else:
                elected = False

            additional_info_dict = {}
            while True:
                additional_info_list = list(input('Введите дополнительные контактные данные через пробел: ').split( ))
                if len(additional_info_list) ==0:
                    break
                else:
                    additional_info_dict[additional_info_list[0]] = additional_info_list[1]
                    additional_info_list.clear()
            new_contact = phones_list[0].add_new_contact(first_name, last_name, phone, elected, **additional_info_dict)
            contact_list.append(new_contact)
            phones_list.append(PhoneBook('Mari_contact_book', contact=contact_list[-1]))
        elif user_input == '3':
            user_input = input('Введите номер телефона, чьей контакт нужно удалить: ')
            for phone in phones_list:
                phone.remove_contact(user_input)
            print('Контакт удален')
        elif user_input == '4':
            for phone in phones_list:
                phone.search_elected()
        elif user_input == '5':
            user_input = input('Введите имя и фамилию через пробел: ').split()
            for phone in phones_list:
                phone.search_for_contact_by_names(user_input)

        elif user_input == 'q':
            break
        else:
            print('Неверная команда')

main()

# contact_dict = {'contact_1': {'Имя': 'Jhon',
#                               'Фамилия': 'Smith',
#                               'Телефон': '71234567809',
#                               'В избранных': 'False',
#                               'Дополнительная информация': {'telegram': '@jhony', 'email': 'jhony@smith.com'}},
#                 'contact_2': {'Имя': 'Anna',
#                               'Фамилия': 'Smith',
#                               'Телефон': '71234567800',
#                               'В избранных': 'False',
#                               'Дополнительная информация': {'telegram': '@Anna', 'email': 'Anna@smith.com'}},
#                 'contact_3': {'Имя': 'Natali',
#                               'Фамилия': 'Smith',
#                               'Телефон': '71234567804',
#                               'В избранных': 'False',
#                               'Дополнительная информация': {'telegram': '@Natali', 'email': 'Natali@smith.com'}}}


# for item in contact_dict:
#     print(item)
#     for item_2 in contact_dict[item]:
#         if item_2 == 'Дополнительная информация':
#            print('telegram=', contact_dict[item][item_2]['telegram'],
#                  'email=', contact_dict[item][item_2]['email'])
#         else:
#             print(contact_dict[item][item_2])
# contact_list.append(Contact())