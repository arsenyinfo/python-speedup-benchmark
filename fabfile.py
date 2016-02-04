# -*- coding: utf-8 -*-

from fabric.api import local
import os
import time


def clean_dir():
    for filename in os.listdir('./'):
        if not any(map(lambda x: filename.endswith(x), ('.pyx', '.py', '.txt', '.md', '.git'))):
            local('rm -r {}'.format(filename))

def go():
    clean_dir()

    commands = (
        'python function.py',
        'python3 function.py',
        'pypy function.py',
        'nuitka --recurse-none function_nuitka_rnone.py',
        './function_nuitka_rnone.exe',
        'nuitka --recurse-all function_nuitka_rall.py',
        './function_nuitka_rall.exe',
        'mv tmp_function_source.pyx function_source.pyx',
        'python function_build.py build_ext --inplace',
        'mv function_source.pyx tmp_function_source.pyx',
        'python function_cython.py',
    )

    with open('result.txt', 'w') as result:
        for command in commands:
            for function in ('generate', 'analyze',):
                local_command = command.replace('function', function)

                ts = time.time()
                local(local_command)
                te = time.time()

                result.write('{};{};{}\n'.format(function, command, te - ts))

            if 'data.json' in os.listdir('./'):
                local('rm data.json')

    clean_dir()