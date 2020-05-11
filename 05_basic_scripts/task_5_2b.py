# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

ip, network = argv[1].split('/')
bin_network = '1' * int(network) + '0' * (32 - int(network))
IP = ip.split('.')

mask_oct1 = int(bin_network[0:8], 2)
mask_oct2 = int(bin_network[8:16], 2)
mask_oct3 = int(bin_network[16:24], 2)
mask_oct4 = int(bin_network[24:], 2)

net_octet1 = int(IP[0]) & mask_oct1
net_octet2 = int(IP[1]) & mask_oct2
net_octet3 = int(IP[2]) & mask_oct3
net_octet4 = int(IP[3]) & mask_oct4

result = (f'\nNetwork:\n'
          f'{int(net_octet1):<10}{int(net_octet2):<10}{int(net_octet3):<10}{int(net_octet4):<10}\n'
          f'{int(net_octet1):08b}  {int(net_octet2):08b}  {int(net_octet3):08b}  {int(net_octet4):08b}\n'
          f'\n'
          f'Mask:\n'
          f'/{network}\n'
          f'{int(mask_oct1):<10}{int(mask_oct2):<10}{int(mask_oct3):<10}{int(mask_oct4):<10}\n'
          f'{int(mask_oct1):08b}  {int(mask_oct2):08b}  {int(mask_oct3):08b}  {int(mask_oct4):08b}\n')

print(result)
