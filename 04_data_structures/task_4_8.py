# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в двоичный формат и вывести на стандартный поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = '192.168.3.1'
oct1, oct2, oct3, oct4 = ip.split('.')
result = (f'{oct1:<10}{oct2:<10}{oct3:<10}{oct4:<10}\n'
          f'{int(oct1):08b}  {int(oct2):08b}  {int(oct3):08b}  {int(oct4):08b}')
print(result)
