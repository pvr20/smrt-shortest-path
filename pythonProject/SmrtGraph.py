import sys

import pprint
from collections import defaultdict


class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        if self._directed:
            self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]

    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(len(list(self._graph.keys()))):
            print(list(self._graph.keys())[node], "t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
        for v in range(len(list(self._graph.keys()))):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * len(list(self._graph.keys()))
        dist[list(self._graph.keys()).index(src)] = 0
        sptSet = [False] * len(list(self._graph.keys()))

        #* list(self._graph.keys())

        for cout in range(len(list(self._graph.keys()))):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for vertex in list(self._graph[list(self._graph.keys())[u]]):
                if vertex in list(self._graph.keys()):
                    v = list(self._graph.keys()).index(vertex)
                    if sptSet[v] == False and dist[v] > dist[u] + 1:
                        dist[v] = dist[u] + 1
        print("Final values "+str(dist))
        self.printSolution(dist)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))