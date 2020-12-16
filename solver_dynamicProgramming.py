#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from timeit import default_timer as timer

Item = namedtuple("Item", ['index', 'value', 'weight'])


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))

    taken = [0] * len(items)
    K = []

    prev = timer()
    # Cálculo de la mochila óptima
    for i in range(item_count+1):
        K.append([])
        for j in range(capacity+1):
            K[i].append(0)

    for i in range(1,item_count+1):
        for j in range(capacity+1):
            if items[i-1].weight <= j:
                K[i][j] = max(items[i-1].value + K[i-1][j-items[i-1].weight], K[i-1][j])
            else:
                K[i][j] = K[i-1][j]
    # Búsqueda de elementos que conforman la mochila óptima
    i = item_count
    j = capacity

    while i > 0 and j > 0:
        if K[i][j] != K[i-1][j]:
            taken[i-1] = 1
            j = j - items[i-1].weight
            i = i-1
        else:
            i = i-1
    print("Tiempo (s): " + str(timer()-prev))
    # prepare the solution in the specified output format
    output_data = str(K[item_count][capacity]) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print(
            'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

