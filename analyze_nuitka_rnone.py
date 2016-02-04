# -*- coding: utf-8 -*-

import json
from math import exp
from string import ascii_letters


def sigmoid(x):
    return 1 / (1 + exp(-x))


def analyze():
    with open('data.json') as rows:
        header = json.loads(rows.readline())

        str_keys = [k for k in header.keys() if k.startswith('str_')]
        int_keys = [k for k in header.keys() if k.startswith('int_')]

        str_result = {k: {letter: 0 for letter in ascii_letters} for k in str_keys}
        int_result = {k: [] for k in int_keys}

        for row in rows:
            row = json.loads(row)
            for k in str_keys:
                for letter in row[k]:
                    str_result[k][letter] += 1
            for k in int_keys:
                int_result[k].append(sigmoid(row[k]))

    str_result = {k: max(str_result[k], key=str_result[k].get) for k in str_keys}
    int_result = {k: sum(int_result[k]) / len(int_result[k]) for k in int_keys}

    return str_result, int_result


if __name__ == '__main__':
    print(analyze())
