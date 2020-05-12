# Neighborhood Growth 

import random
import itertools
import collections
import numpy as np

class Dynamics:

    def __init__(self, young_diagram, site_configuration):
        self.young_diagram = self.zero_set(young_diagram)
        self.site_configuration = self.normalize_site_configuration(site_configuration)
        self.make_bounding_box()

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
            self.bounding_box.append([False]*(bounding_box_width+1))
        for (i,j) in self.site_configuration:
            self.bounding_box[j][i] = True

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
        updated_bounding_box = []
        maximum_x_value = max(map(lambda t: t[0], self.site_configuration))
        maximum_y_value = max(map(lambda t: t[1], self.site_configuration))
        bounding_box_width = 2 * maximum_x_value + 1
        bounding_box_height = 2 * maximum_y_value + 1
        for i in range(0,bounding_box_height + 1):
            updated_bounding_box.append([False]*(bounding_box_width + 1))
        for j in range(0,bounding_box_height + 1):
            for i in range(0,bounding_box_width + 1):
                # print("x", (i,j))
                # print(updated_bounding_box[j][i])
                # print(self.bounding_box[j][i])
                updated_bounding_box[j][i] = self.bounding_box[j][i] or not self.turn_on(i,j)
                # updated_bounding_box[j][i] = self.bounding_box[j][i] or self.turn_on(i,j) 
        self.bounding_box = updated_bounding_box


def threshold_set(n):
    threshold_diagram = []
    for i in range(1,n+1):
        threshold_diagram.append(n + 1 - i)
    return threshold_diagram

def sumadd(n):
    sum = (n*(n+1))/2
    return sum

def thin_set(n):
    thinset = []
    for i in range(n):
        for j in range(n + sumadd(n-i-1), n + sumadd(n-i-1) + (n-i)):
            thinset.append((i,j))
            thinset.append((j,i))
    return thinset


zeroset = threshold_set(8)
thinset = thin_set(4)
test = Dynamics(zeroset, thinset)
print(test.bounding_box)
for i in range(0,9):   
    test.transform()
    print(test.bounding_box)




# Young diagram by list