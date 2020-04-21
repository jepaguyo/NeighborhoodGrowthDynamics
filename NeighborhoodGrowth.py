# Neighborhood Growth 

import random
import itertools
import collections
import numpy as np

class Dynamics:

    def __init__(self, young_diagram, site_configuration):
        self.young_diagram = young_diagram
        self.site_configuration = self.normalize_site_configuration(site_configuration)

    def normalize_site_configuration(self, site_configuration): 
        minimum_x_value = min(map(lambda t: t[0], site_configuration))
        minimum_y_value = min(map(lambda t: t[1], site_configuration))
        shift = lambda t: (t[0] - minimum_x_value, t[1] - minimum_y_value)
        return list(map(shift, site_configuration))

print (Dynamics([], [(2,5), (-3,1), (8, 5), (4,7)]).site_configuration)


# Young diagram by list