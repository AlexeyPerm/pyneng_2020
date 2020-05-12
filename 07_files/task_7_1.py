# -*- coding: utf-8 -*-
"""
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

with open('ospf.txt', 'r') as file:
    for line in file:
        protocol, prefix, ad, _, nexthop, last_update, out_int = line.rstrip().split()
        ad_metric = ad.strip('[]')
        protocol = protocol + 'spf'
        result = (f"Protocol:              {protocol}\n"
                  f"Prefix:                {prefix}\n"
                  f"AD/Metric:             {ad_metric}\n"
                  f"Next-Hop:              {nexthop}\n"
                  f"Last update:           {last_update}\n"
                  f"Outbound Interface:    {out_int}\n")
        print(result)
