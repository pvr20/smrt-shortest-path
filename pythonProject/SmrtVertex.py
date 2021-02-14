import sys

import pprint
from collections import defaultdict


class Vertex(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, name, code):
        self.name = name
        self.code = code


    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Vertex):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(str(self.name))

    def __str__(self):
        return '{}({})'.format(self.name, self.code)