# Neighborhood Growth 

import random
import itertools
import collections
import numpy as np

class Dynamics:

    def __init__(self, young_diagram, site_configuration):
        self.young_diagram = self.zero_set(young_diagram)
        self.site_configuration = self.normalize_site_configuration(site_configuration)

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


def threshold_set(n):
    threshold_diagram = []
    for i in range(1,n+1):
        threshold_diagram.append(n + 1 - i)
    return threshold_diagram

zeroset = threshold_set(5)
# zeroset = [4,3,2,1]
print (Dynamics(zeroset, [(2,5), (-3,1), (8, 5), (4,7)]).site_configuration)
print (Dynamics(zeroset, [(2,5), (-3,1), (8, 5), (4,7)]).young_diagram)


# Young diagram by list