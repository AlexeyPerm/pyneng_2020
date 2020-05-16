# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def str_to_list(string, trunk=True):
    """
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
            elif 'access vlan' in line:
                access_dict[intf] = str_to_list(line, trunk=False)
            elif 'trunk allowed' in line:
                trunk_dict[intf] = str_to_list(line)
    return access_dict, trunk_dict


print(get_int_vlan_map(config_filename='config_sw1.txt'))
