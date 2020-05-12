# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

ignore = ['duplex', 'alias', 'Current configuration']

with open(argv[1]) as file, open(argv[2], 'w') as dst:
#with open('config_sw1.txt') as file, open('ololo.txt', 'w') as dst:
    for line in file:
        for k in ignore:
            if k in line:
                break
        else:
            dst.write(line)
