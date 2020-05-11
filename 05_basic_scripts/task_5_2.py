# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip, network = input('Введите ip-сеть в формате ip/network: ').split('/')

bin_network = '1' * int(network) + '0' * (32 - int(network))
IP = ip.split('.')

mask_oct1 = int(bin_network[0:8], 2)
mask_oct2 = int(bin_network[8:16], 2)
mask_oct3 = int(bin_network[16:24], 2)
mask_oct4 = int(bin_network[24:], 2)

result = (f'Network:\n'
          f'{int(IP[0]):<10}{int(IP[1]):<10}{int(IP[2]):<10}{int(IP[3]):<10}\n'
          f'{int(IP[0]):08b}  {int(IP[1]):08b}  {int(IP[2]):08b}  {int(IP[3]):08b}\n'
          f'\n'
          f'Mask:\n'
          f'/{network}\n'
          f'{int(mask_oct1):<10}{int(mask_oct2):<10}{int(mask_oct3):<10}{int(mask_oct4):<10}\n'
          f'{int(mask_oct1):08b}  {int(mask_oct2):08b}  {int(mask_oct3):08b}  {int(mask_oct4):08b}\n')

print(result)
