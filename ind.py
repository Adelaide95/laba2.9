# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def pretty_print(x):
    if x[0] != len(x):
        res = str(x[0])
        x = x[1:]
        for elem in x:
            if elem:
                res += " + " + str(elem)
        print(res)
    else:
        print(x[0])


def part(pos, max_slag_pos, number):
    global x
    if number == 0:
        pretty_print(x)
        if pos != 0:
            x = x[:pos - 1] + [0] * (len(x) - pos + 1)
    else:
        for i in range(1, min(max_slag_pos + 1, number + 1)):
            x[pos] = i
            part(pos + 1, i, number - i)


n = int(input("Введите число: "))
x = [0] * n
part(0, n, n)
