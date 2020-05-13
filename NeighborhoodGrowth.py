# Neighborhood Growth 

from __future__ import print_function

import random
import itertools
import collections
import numpy as np

class Dynamics:

    def __init__(self, young_diagram, site_configuration):
        self.young_diagram = self.zero_set(young_diagram)
        self.site_configuration = self.normalize_site_configuration(site_configuration)
        self.make_bounding_box()
        self.generation = 0

    def normalize_site_configuration(self, site_configuration): 
        minimum_x_value = min(map(lambda t: t[0], site_configuration))
        minimum_y_value = min(map(lambda t: t[1], site_configuration))
        shift = lambda t: (t[0] - minimum_x_value, t[1] - minimum_y_value)
        return list(map(shift, site_configuration))

    def zero_set(self, young_diagram):
        growth_sites = []
        for i in range(0,len(young_diagram)):
            for j in range(0,young_diagram[i]):
                growth_sites.append((j,i))
        return growth_sites

    def make_bounding_box(self):
        maximum_x_value = max(map(lambda t: t[0], self.site_configuration))
        maximum_y_value = max(map(lambda t: t[1], self.site_configuration))
        bounding_box_width = 2 * maximum_x_value + 1
        bounding_box_height = 2 * maximum_y_value + 1
        self.bounding_box = []
        for i in range(0,bounding_box_height + 1):
            self.bounding_box.append([0]*(bounding_box_width+1))
            #self.bounding_box.append([' ']*(bounding_box_width+1))
        for (i,j) in self.site_configuration:
            #self.bounding_box[j][i] = 1
            self.bounding_box[j][i] = 'x'

    def row_count(self, row_index):
        count = 0
        for on in self.bounding_box[row_index]:
            if on:
                count += 1
        return count

    def col_count(self, col_index):
        count = 0
        for row in self.bounding_box:
            if row[col_index]:
                count += 1
        return count 

    def turn_on(self, i, j):
        row_c = self.row_count(j)
        col_c = self.col_count(i)
        return (row_c, col_c) in self.young_diagram

    def transform(self): 
        self.generation += 1
        updated_bounding_box = []
        maximum_x_value = max(map(lambda t: t[0], self.site_configuration))
        maximum_y_value = max(map(lambda t: t[1], self.site_configuration))
        bounding_box_width = 2 * maximum_x_value + 1
        bounding_box_height = 2 * maximum_y_value + 1
        for i in range(0,bounding_box_height + 1):
            updated_bounding_box.append([0]*(bounding_box_width + 1))
        for j in range(0,bounding_box_height + 1):
            for i in range(0,bounding_box_width + 1):
                if self.bounding_box[j][i]:
                    updated_bounding_box[j][i] = self.bounding_box[j][i]
                elif not self.turn_on(i,j): 
                    updated_bounding_box[j][i] = self.generation
        self.bounding_box = updated_bounding_box

    def spans(self):
        previous_state = []
        count = 0
        while self.bounding_box != previous_state: 
            previous_state = self.bounding_box
            self.transform()
            count += 1
        if all(all(line) for line in self.bounding_box):
            return (count-1)
        else:
            return all(all(line) for line in self.bounding_box)



# Initialize a threshold zero set
def threshold_set(n):
    threshold_diagram = []
    for i in range(1,n+1):
        threshold_diagram.append(n + 1 - i)
    return threshold_diagram

# Add integers from 1 to n
def sumadd(n):
    sum = (n*(n+1))/2
    return sum

# Initialize a thin set
def thin_set(n):
    thinset = []
    if n%2 == 0:
        m = n/2
        for i in range(m):
            for j in range(m + sumadd(m-i-1), m + sumadd(m-i-1) + (m-i)):
                thinset.append((i,j))
                thinset.append((j,i))
    else:
        p = n/2
        m = n/2 + 1
        for k in range(1 + p + sumadd(p), 2 + p + sumadd(p) + p):
            thinset.append((0,k))
        for i in range(1,m+1):
            for j in range(m + sumadd(m-i-1), m + sumadd(m-i-1) + (m-i)):
                thinset.append((i,j))
                thinset.append((j,i))
    return thinset

def line_to_string(line):
    string_line = map(str,line)
    return " ".join(string_line)



zeroset = threshold_set(12)
thinset = thin_set(12)
# thinset = [(0,5), (0,6), (0,7), (1,4), (1,3), (2,2), (3,1), (4,0), (5,0)]
test = Dynamics(zeroset, thinset)

# for i in test.bounding_box:
#     print i
# lines = list(map(lambda x : " ".join(x), test.bounding_box))
# print(*lines, sep = "\n")

# test.transform()
# test.transform()
# print(*test.bounding_box, sep = "\n")

# print(line_to_string([1, "a", True]))


lines = list(map(line_to_string, test.bounding_box))
print(*lines, sep = "\n")
print("\n")
for i in range(0,14):   
    test.transform()
    lines = list(map(line_to_string, test.bounding_box))
    print(*lines, sep = "\n")
    print("\n")

# print(test.spans())
# lines = list(map(line_to_string, test.bounding_box))
# print(*lines, sep = "\n")

