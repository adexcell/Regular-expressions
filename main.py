import csv
import re

from pprint import pprint


def open_csv():
    with open('phonebook_raw.csv', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def rewriting_fio(contacts_list):
    for contact in contacts_list[1:]:
        position_1 = contact[0].split(' ')
        if len(position_1) == 3:
            contact[0] = position_1[0]
            contact[1] = position_1[1]
            contact[2] = position_1[2]
        elif len(position_1) == 2:
            contact[0] = position_1[0]
            contact[1] = position_1[1]
        else:
            pass
        position_2 = contact[1].split(' ')
        if len(position_2) == 2:
            contact[1] = position_2[0]
            contact[2] = position_2[1]
        else:
            pass
    return contacts_list


def pretty_phone(some_list):
    pattern_to_find = re.compile(
        '(\+?\d)(\s{0,3})\(?(\d{3})\)?(\s{0,3})\-?(\d{3})\-?(\d{2})\-?(\d{2})(\s{0,3})\(?(доб.)?(\s{0,3})(\d{4})?\)?'
        )
    for contact in some_list:
        if 'доб.' in contact[-2]:
            new_phone = pattern_to_find.sub(r'+7(\3)\5-\6-\7 доб.\11', contact[-2])
        else:
            new_phone = pattern_to_find.sub(r'+7(\3)\5-\6-\7', contact[-2])
        contact[-2] = new_phone
    return some_list


def del_duplicates(some_list):
    in_list = list()
    clean_phonebook = list()
    clean_phonebook.append(some_list[0])
    for contact in sorted(some_list[1:]):
        if contact[0] in in_list:
            for clean_contact in sorted(clean_phonebook):
                if clean_contact[0] == contact[0]:
                    counter = 0
                    for value in contact:
                        if value in clean_contact:
                            counter += 1
                            pass
                        else:
                            clean_contact[counter] = value
                            counter += 1
                else:
                    pass
        else:
            clean_phonebook.append(contact)
            in_list.append(contact[0])
    return clean_phonebook


def write_csv(ready_list):
    with open("pretty_phonebook.csv", "w", encoding='UTF-8') as f:
        data_writer = csv.writer(f, delimiter=',')
        data_writer.writerows(ready_list)


if __name__ == '__main__':
    contacts_list = open_csv()
    pretty_fio_list = rewriting_fio(contacts_list)
    pretty_phones_list = pretty_phone(pretty_fio_list)
    clean_list = del_duplicates(pretty_phones_list)
    pprint(clean_list)
    write_csv(clean_list)
