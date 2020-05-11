# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

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

net_octet1 = int(IP[0]) & mask_oct1
net_octet2 = int(IP[1]) & mask_oct2
net_octet3 = int(IP[2]) & mask_oct3
net_octet4 = int(IP[3]) & mask_oct4

result = (f'Network:\n'
          f'{int(net_octet1):<10}{int(net_octet2):<10}{int(net_octet3):<10}{int(net_octet4):<10}\n'
          f'{int(net_octet1):08b}  {int(net_octet2):08b}  {int(net_octet3):08b}  {int(net_octet4):08b}\n'
          f'\n'
          f'Mask:\n'
          f'/{network}\n'
          f'{int(mask_oct1):<10}{int(mask_oct2):<10}{int(mask_oct3):<10}{int(mask_oct4):<10}\n'
          f'{int(mask_oct1):08b}  {int(mask_oct2):08b}  {int(mask_oct3):08b}  {int(mask_oct4):08b}\n')

print(result)
