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
oct1, oct2, oct3, oct4 = ip.split('.')
first_oct_m = int(bin_network[0:8], 2)
second_oct_m = int(bin_network[8:16], 2)
third_oct_m = int(bin_network[16:24], 2)
fourth_oct_m = int(bin_network[24:], 2)


result = (f"Network:\n"
          f"{oct1:<10}{oct2:<10}{oct3:<10}{oct4:<10}\n"
          f"{int(oct1):08b}  {int(oct2):08b}  {int(oct3):08b}  {int(oct4):08b}\n"
          f"\n"
          f"Mask:\n"
          f"/{network}\n"
          f"{first_oct_m:<10}{second_oct_m:<10}{third_oct_m:<10}{fourth_oct_m:<10}\n"
          f"{first_oct_m:<10b}{second_oct_m:<10b}{third_oct_m:<10b}{fourth_oct_m:<10b}"
          )

print(result)
