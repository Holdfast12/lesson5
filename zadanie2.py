#!/usr/bin/python3
#Написать функцию, принимающую сколько угодно параметров (в том числе и 0) и возвращающую их сумму.

import re

def summ(*args):
    print(sum(args))

while True:
    print(list(map(lambda n: float(n) if '.' in n else int(n), (input('\nВведите параметры для сложения: ').split()))))
