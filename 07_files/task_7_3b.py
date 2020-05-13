# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

result = []

with open('CAM_table.txt') as src:
    for line in src:
        if 'DYNAMIC' in line:
            a = line.split()
            a[0] = int(a[0])
            result.append(a)

a = int(input('Введите номер влана: '))
for k in result:
    if k[0] == a:
        print(f' {k[0]:<9}{k[1]}   {k[3]}')
