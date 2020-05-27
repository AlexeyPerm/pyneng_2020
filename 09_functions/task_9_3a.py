# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint

def str_to_list(string, trunk=True):
    """
    Функция сделана, потому что захотел.
    При истинном параметре "trunk" возвращает список чисел из строки вида
    "switchport trunk allowed vlan 100,300,400,500,600 "
    Результат: [100, 300, 400, 500, 600]
    Если ложь, значит порт в режиме access и строка имеет вид "switchport access vlan 10". Возвращает просто число 10.
    """
    if trunk:
        str_line = string.strip().split()[-1]
        # строка, если мы типа не читали раздел "Полезные функции"
        # result = [int(k) for k in str_line.split(',')]
        result = list(map(int, str_line.split(",")))
    else:
        result = int(string.strip().split()[-1])
    return result


def get_int_vlan_map(config_filename):
    trunk_dict = {}
    access_dict = {}
    with open(config_filename, 'r') as f:
        for line in f:
            if 'Ethernet' in line:
                intf = line.strip().split()[-1]
                a = f.readline()
                if 'mode access' in a:
                    access = f.readline()
                    if 'access vlan' in access:
                        access_dict[intf] = str_to_list(access, trunk=False)
                    elif 'duplex auto' in access:
                        access_dict[intf] = 1
                elif 'encapsulation dot1q' in a:
                    trunk = f.readline()
                    trunk_dict[intf] = str_to_list(trunk)

    return access_dict, trunk_dict


pprint(get_int_vlan_map(config_filename='config_sw2.txt'))