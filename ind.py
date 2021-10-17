#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fun(n, list_n):
    if n == 0:
        print(list_n[1], end='')
        for i in list_n[2:]:
            print(f'+{i}', end='')
        print('')
    else:
        x = list_n[len(list_n) - 1]
        if n >= x:
            for i in range(max(1, x), n + 1):
                fun(n - i, list_n + [i])


if __name__ == '__main__':
    num = int(input('Введите число: '))
    fun(num, [0])
