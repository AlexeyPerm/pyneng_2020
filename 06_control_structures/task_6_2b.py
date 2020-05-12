# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Ввериде ip-адрес: ')
correct = True

while not correct:
    if ip.count('.') != 3:
        correct = False
    elif correct:
        for k in ip.split('.'):
            if int(k) not in range(0, 256):
                correct = False
                break

if correct:
    first_byte = int(ip.split('.')[0])
    if 1 <= first_byte <= 223:
        print('unicast')
    elif 224 <= first_byte <= 239:
        print('multicast')
    elif ip == '255.255.255.255':
        print('local broadcast')
    elif ip == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
else:
    print('Неправильный IP-адрес')