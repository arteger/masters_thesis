#!usrbinenv python

from json import load
from sys import argv


def loc(nb):
    with open(nb, encoding='utf-8') as data_file:
        cells = load(data_file)['cells']
        return sum(len(c['source']) for c in cells if c['cell_type'] == 'code')


def run(ipynb_files):
    return sum(loc(nb) for nb in ipynb_files)


if __name__ == '__main__':
    print(run(["main.ipynb"]))
