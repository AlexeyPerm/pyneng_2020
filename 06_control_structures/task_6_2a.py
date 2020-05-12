# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ip = input('Ввериде ip-адрес: ')
correct = True

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