# -*- coding: utf-8 -*-

from random import choice, randint
from string import ascii_letters
from itertools import permutations
import json


def create_string(l=8):
    return ''.join([choice(ascii_letters) for _ in range(l)])


def generate(keys=5, samples=500000):
    str_keys = ['str_{}'.format(create_string()) for _ in range(keys)]
    int_keys = ['int_{}'.format(create_string()) for _ in range(keys)]

    with open('data.json', 'w') as output:
        for _ in range(samples):
            row = {}
            for k in int_keys:
                row[k] = randint(0, 100) / 100.0
            for k in str_keys:
                row[k] = ''.join(permutations(create_string(15), 12).next())

            output.write('{}\n'.format(json.dumps(row)))


if __name__ == '__main__':
    generate()
